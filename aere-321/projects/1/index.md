# AERE 321 Project 1

I chose to do this project in Python since it features modern abstractions like classes and enums, much like other languages of my liking like TypeScript, Go, C#, Rust, etc. Also please keep in mind that since Python is a 0-indexed language, my member and joint ids start from 0 instead of 1, unlike what was prescribed to us in the Project 1 document. I have taken taken the liberty of re-annotating the figure with my indexing:

![](https://i.imgur.com/VBblIGA.png)

And of course, here is the figure with the external forces and moments:

![](https://i.imgur.com/rZ0rYBe.png)

## The Code

I have create the following classes for describing the structure of the beam, solving the matrices, rendering the intermediate representations, and printing the final results, all commented to the best of my abilities:

> [!NOTE]
> These are just the abstractions! You won't see anything if you run this file. Refer to the rest of this document to see how I designed these classes to be used.

```py
# I am using numpy to handle matrices; there's no need for me to make my own
# implementation.
import numpy as np

# Enums are great for discrimination in TypeScript and Rust. Python doesn't
# have them out of the box, but there's a class.
from enum import Enum

# Numpy's print width was too narrow to fit big matrices so I changed it.
np.set_printoptions(linewidth=200)


# The support type discriminator. Logic later uses this to figure out what's
# fixed and free.
class SupportType(Enum):
    NONE = 1
    FIXED = 2
    ROLLER = 3


# This is a purely nominal class that I use for interfacing with the Beam class
# later.
class Support:
    def __init__(self, x: float, type: SupportType):
        self.type = type
        self.x = x


# Another enum, this time for the external force or moment type.
class ExternalType(Enum):
    FORCE = 1
    MOMENT = 2


# Another nominal class without methods. The held values here will be used in
# logic below.
class External:
    def __init__(self, x: float, type: ExternalType, value: float):
        self.x = x
        self.type = type
        self.value = value


# Finally, a class with methods! This class represents the joint between two
# members.
class Joint:
    # A joint can only have 1 support, but any number of external moments and
    # forces.
    def __init__(self, support: Support, externals: list[External]):

        # Store the support.
        self.support = support

        # Filter forces and moments into separate lists.
        external_forces = [
            external for external in externals if external.type == ExternalType.FORCE
        ]
        external_moments = [
            external for external in externals if external.type == ExternalType.MOMENT
        ]

        # Find resultants and store them.
        self.external_force = sum([external.value for external in external_forces])
        self.external_moment = sum([external.value for external in external_moments])

        # Also cache the freedoms of the joint to avoid recomputing them.
        self.free_displacement = support.type == SupportType.NONE
        self.free_rotation = support.type != SupportType.FIXED

    # This is a part of the debug renderer which draws the beam in the console.
    # The joint renders a pipe ( |) and the support type which can either be a
    # fixed block (░░) or a roller (◯|). In the case of a free joint, the pipe
    # us left alone.
    def render(self):

        # Default to a pipe.
        icon = " |"

        # Turn pipe into a fixed support.
        if self.support.type == SupportType.FIXED:
            icon = "░░"
        elif self.support.type == SupportType.ROLLER:
            icon = "◯|"

        # Print the joint type and external forces and moments.
        print(f"{icon} → {self.external_force} ⭯ {self.external_moment}")

    # Print P_i and P_i+1.
    def print_loads(self, id: int):
        print(f"P_{id} = {self.external_force}")
        print(f"P_{id + 1} = {self.external_moment}")


# This class represents members that sit between two joints.
class Member:
    # Members accept an id, starting from 0 because it's Python, the x position
    # of the left end of the member, E and I of the material, L of the member
    # (not the whole beam, that was a nasty bug!), and the left and right
    # joints. The left joint is the same as the right joint for the last member
    # and vice versa.
    def __init__(
        self, id: int, x: float, E: float, I: float, L: float, left: Joint, right: Joint
    ):
        # Store the values.
        self.id = id
        self.x = x

        self.E = E
        self.I = I
        self.L = L

        self.left = left
        self.right = right

    # Computing the k value is a method here and not a part of __init__ because
    # this class is always initialized with a dummy joint for the right side of
    # the beam which is later replaced with a real joint when the left joint of
    # the next member is initialized.
    def k(self):

        # Declare local variables for ease of reading.
        E = self.E
        I = self.I
        L = self.L

        # The goofy matrix from lecture.
        return ((E * I) / L**3) * np.matrix(
            [
                [12, 6 * L, -12, 6 * L],
                [6 * L, 4 * L * L, -6 * L, 2 * L * L],
                [-12, -6 * L, 12, -6 * L],
                [6 * L, 2 * L * L, -6 * L, 4 * L * L],
            ]
        )

    # The k matrix is normally trimmed. For instance, the k matrix of member
    # a joint of displacement id 3 will have the 3rd id in the first two (index
    # of 0). So, we need to pad.
    def k_padded(self, max_id: int):

        # Rows and columns to pad above and below was an interesting algebraic
        # problem. Fortunately, when I switched to 0-based indexing, it became
        # much easier.
        top_left_padding = 2 * self.id
        bottom_right_padding = 2 * (max_id - self.id)

        # Numpy has a built-in function for padding matrices.
        return np.pad(
            self.k(),
            pad_width=(
                (top_left_padding, bottom_right_padding),
                (top_left_padding, bottom_right_padding),
            ),
        )

    # The u matrix is a subset of the full d column vector.
    def u(self, d: np.matrix):

        # This is the most clever thing I have come up with Python by far. The
        # range(4) produces values from 0 to 3 (inclusive). Then, I just add it
        # to the double of the member id, which turns out is the first id of the
        # left joint since we are using 0-based indexing.
        slice = [self.id * 2 + index for index in range(4)]

        # Numpy has a built-in function for slicing matrices.
        return d[np.ix_(slice)]

    # Printed for the u matrix just denotes the subscript and prints the raw
    # matrix.
    def print_u(self, d: np.matrix):
        print(f"u_{self.id} =")
        self.print_indices()
        print(self.u(d), end="\n\n")

    # Q is as simple as k * u. Not much to say here.
    def Q(self, d: np.matrix):
        u = self.u(d)
        return self.k() * u

    # Before Q can be globally manipulated, it needs to be padded. It uses the
    # same padding as k_padded but with some simplification since its a column
    # vector.
    def Q_padded(self, d: np.matrix, max_id: int):
        top_padding = 2 * self.id
        bottom_padding = 2 * (max_id - self.id)

        return np.pad(
            self.Q(d),
            pad_width=(
                (top_padding, bottom_padding),
                (0, 0),
            ),
        )

    # Same deal. Prints Q with a label of the correct subscript.
    def print_Q(self, d: np.matrix):
        print(f"Q_{self.id} =")
        self.print_indices()
        print(self.Q(d), end="\n\n")

    # Renders the intermediate pipe (|) symbols between the joint along with
    # the id, x position, and length of the member.
    def render(self):
        self.left.render()

        print(" |")
        print(f" | #{self.id} x={self.x} L={self.L}")
        print(" |")

    def print_indices(self):
        print(f"(indices: {", ".join([str(i + self.id * 2) for i in range(4)])})")

    # The k matrix is printed for each member with the correct label.
    def print_k(self):
        print(f"k_{self.id} =")
        self.print_indices()
        print(self.k(), end="\n\n")


# The beam is a collection of members.
class Beam:
    # The beam accepts material properties and a list of supports and external
    # forces and moments.
    def __init__(self, E, I, L, supports: list[Support], externals: list[External]):

        # Simply store the values.
        self.E = E
        self.I = I
        self.L = L

        self.supports = supports
        self.externals = externals

        # Break points is clever because I found out Python has sets much
        # like Set<number>() in TypeScript. This lets me collect all candidates
        # for where I can split the beam into members. The points of interest
        # include the start and end of the beam as a default in the off case
        # the beam has literally no supports or externals.
        break_points_pool = {0, self.L}

        # Loop though all supports, regardless of type, and add it to the set.
        # And since sets in Python work much like Set() from TypeScript, any
        # duplicates will be ignored. So we end up with a unique set of points.
        for support in self.supports:
            break_points_pool.add(support.x)

        # Same deal for externals.
        for external in self.externals:
            break_points_pool.add(external.x)

        # The points will likely be out of order so I sort them into a proper
        # list.
        self.break_points = sorted(list(break_points_pool))

        # This is the juicy function that's tricky to get right. Thankfully,
        # 0-based indexing makes it trivial.
        # The first member id is 0.
        member_id = 0

        # An empty list to hold the members.
        self.members: list[Member] = []

        # Loop through the break points which represent the position of the
        # left side of the members (thus, by extension, the left joints).
        for x in self.break_points:

            # Store this info since I will use it multiple times.
            is_first = member_id == 0
            is_last = member_id == len(self.break_points) - 1

            # Filter supports and externals that act on the left side of this
            # beam.
            supports = [support for support in self.supports if support.x == x]
            externals = [external for external in self.externals if external.x == x]

            # It makes no physical sense to have more than 1 support on the
            # same point. So I record the length for future consideration.
            supports_length = len(supports)

            # Throw an error (or as it's called in Python, raise and error) if
            # there are more than 1 support.
            if supports_length > 1:
                raise ValueError(f"More than 1 support found at x = {x}")

            # Create the left joint with the appropriate support if available
            # or create a nominal NONE type joint.
            left = Joint(
                supports[0] if supports_length == 1 else Support(x, SupportType.NONE),
                externals,
            )

            # The right hand side is a dummy awaiting to be replaced by the
            # left hand side of the next member.
            right = Joint(Support(x, SupportType.NONE), [])

            # If this is the last index, we are actually dealing with a member
            # beyond the length of the beam. In other words, the left side of
            # this member would at the very right end of the whole beam. So we
            # never create a member if this is the last index.
            if not is_last:

                # Get the next break point to get the length of this member.
                x_next = self.break_points[member_id + 1]

                # Create the segment with the correct values.
                segment = Member(member_id, x, self.E, self.I, x_next - x, left, right)

            # If this is anything but the first member, there exists another
            # member to the left of this one which is awaiting a right side
            # joint. So, I donate the left side of this member to the right
            # side of the previous member.
            if not is_first:
                last_member = self.members[-1]
                last_member.right = left

            if not is_last:
                # Throw it into the list.
                self.members.append(segment)

            # Increment the member id.
            member_id += 1

        # Initialize the set of free indices.
        self.free_indices: list[int] = []
        length = len(self.members)

        # Check the left joint of members to see if they are free.
        for member in self.members:
            if member.left.free_displacement:
                self.free_indices.append(member.id * 2)

            if member.left.free_rotation:
                self.free_indices.append(member.id * 2 + 1)

        # Now check the right joint of the last member to finish up.
        if self.members[-1].right.free_displacement:
            self.free_indices.append(length * 2)

        if self.members[-1].right.free_rotation:
            self.free_indices.append(length * 2 + 1)

        # Store the generated list. These should be in order already so no need
        # to sort.
        self.free_indices = self.free_indices

        # Invert the list to get the fixed indices.
        self.fixed_indices = [
            index
            for index in range(len(self.members) * 2 + 2)
            if index not in self.free_indices
        ]

    # The s, by default, is the sum of all the padded stiffness matrices.
    def s_padded(self):
        max_id = len(self.members) - 1
        return sum([member.k_padded(max_id) for member in self.members])

    # The but padded s is unnecessarily large and can be trimmed down to only
    # include the rows and columns associated with the free indices.
    def s(self):
        return self.s_padded()[np.ix_(self.free_indices, self.free_indices)]

    # P is the sum of all the padded external loads, but stored as a column
    # vector.
    def P_padded(self):

        # The matrix starts off as a list of lists with a single item in them,
        # causing numpy to generate a 1 wide column vector.
        rows: list[list[float]] = []

        # Append forces and then moments for all the left joint of the members.
        for member in self.members:
            rows.append([member.left.external_force])
            rows.append([member.left.external_moment])

        # Same for the right joint of the last member.
        rows.append([self.members[-1].right.external_force])
        rows.append([self.members[-1].right.external_moment])

        # Turn that into a column vector, or technically a matrix.
        return np.matrix(rows)

    # Once again, P_padded includes the fixed indices too so I remove them by
    # pulling out the rows and columns associated with the free indices.
    def P(self):
        return self.P_padded()[np.ix_(self.free_indices)]

    # I use numpy's numerical methods to solve for d because it's faster but
    # for matrices this small, you can also get away with an analytical
    # solution obtained by inverting the s matrix. Also, my code has no support
    # for P_f because I split the beam into members and create joints on all
    # forces, leaving no force to act in the middle of the beam. P_f, this way,
    # is always 0.
    def d(self):
        return np.linalg.solve(self.s(), self.P())

    # When you use the function above, you actually get the d column vector
    # with only columns associated with free indices. I created a method here
    # to re-pad the d vector to include the fixed indices. Of course I insert a
    # 0 for the fixed indices because they are... well... fixed.
    def d_padded(self):

        # I start off with the trimmed d vector.
        d = self.d()

        # And I create a new dictionary to hold the values from the d vector
        # with keys relating to the free indices.
        d_sorted = dict()

        # I then sort the keys into the dictionary.
        index = 0
        for free_index in self.free_indices:
            d_sorted[free_index] = d[index].item()
            index += 1

        # Now, I create a vector, this time with 0s for the fixed indices.
        d_padded: list[list[float]] = []

        # I go through and populate the new inflated column vector, filling it
        # in with 0s if there is no value from the d column vector associated
        # with that fixed index.
        for index in range(len(self.members) * 2 + 2):
            d_padded.append([d_sorted[index] if index in d_sorted else 0])

        # Convert the list to a matrix.
        return np.matrix(d_padded)

    # The reaction forces, R, is the sum of all the Q's from all the members.
    # These Q's come padded with a bunch of 0's by default so that they line
    # up perfectly with one another dimension wise when adding.
    def R_padded(self):
        d_padded = self.d_padded()

        return sum(
            [
                member.Q_padded(d_padded, len(self.members) - 1)
                for member in self.members
            ]
        )

    # All values relating to the free indices will be useless, so we remove
    # them.
    def R(self):
        return self.R_padded()[np.ix_(self.fixed_indices)]

    # These two methods below are just for the project assignment. They remain
    # unused if I ever intend to use this code for personal applications.
    def print_free_indices(self):
        print(f"(indices: {", ".join([str(i) for i in self.free_indices])})")

    def print_fixed_indices(self):
        print(f"(indices: {", ".join([str(i) for i in self.fixed_indices])})")

    # This is the bread and butter of the project. This method used to be huge
    # just yesterday, but I abstracted away a lot of the logic into other
    # methods.
    def solve(self) -> np.matrix:

        # As per the requirements of this assignment, I begin by printing all
        # the k matrices for all the members.
        for member in self.members:
            member.print_k()

        # Then the s matrix.
        print("s =")
        self.print_free_indices()
        print(self.s(), end="\n\n")

        # And then the P. As you can see, the code here is really simple
        # because I moved so much of the logic into other methods.
        print("P =")
        self.print_free_indices()
        print(self.P(), end="\n\n")

        # And finally the d vector.
        print("d =")
        self.print_free_indices()
        print(self.d(), end="\n\n")

        # Now I recreate the d_padded vector with all its extra 0s. This of
        # course is a waste of compute since d_padded was already computed
        # somewhere when calling the d() method, but I only recreate d_padded
        # again for the purposes of logging the values, which is required for
        # the assignment. I will be deleting most of the prints after I turn in
        # the assignment.
        d_padded = self.d_padded()

        # Printing the u and Q matrices actually require a solved solution for
        # the d vector in its padded form.
        for member in self.members:
            member.print_u(d_padded)

        for member in self.members:
            member.print_Q(d_padded)

        # And, finally, the reaction forces.
        print("R =")
        self.print_fixed_indices()
        print(self.R(), end="\n\n")

    # Now, the master renderer. I render all the members one by one which
    # renders their respective left joints and the beam in between, and then I
    # handle the remaining right joint.
    def render(self):
        for member in self.members:
            member.render()

        self.members[-1].right.render()
        print()
```

## Using the Code

One of the most vital things to do is ensure the code has digested the beam correctly and split it into the correct members. To aid my debugging, I made a `beam.render()` method which can be called after initializing an instance of the `Beam` class. Furthermore, the `beam.solve()` method prints every necessary value as required by this assignment.

This is how you can use my `Beam` class to solve the beam for this project (make sure the units are consistent):

```py
beam = Beam(
    150 * 10**6,
    500 * 10**-6,
    20,
    [
        Support(20 * (0 / 5), SupportType.FIXED),
        Support(20 * (1 / 5), SupportType.ROLLER),
        Support(20 * (3 / 5), SupportType.ROLLER),
        Support(20 * (4 / 5), SupportType.ROLLER),
    ],
    [
        External(20 * (1 / 5), ExternalType.MOMENT, 100),
        External(20 * (2 / 5), ExternalType.FORCE, -350),
        External(20 * (3 / 5), ExternalType.MOMENT, -100),
        External(20 * (5 / 5), ExternalType.FORCE, -200),
    ],
)
```

After declaring the beam class, you can call the `beam.render()` method to ensure the beam is split correctly. In the case of this project, I indeed get an output that matches my diagram above. Note the correct roller and fixed supports and the correct external moments and forces at the right joints and offsets from the y-axis.

```
░░ → 0 ⭯ 0
 |
 | #0 x=0 L=4.0
 |
◯| → 0 ⭯ 100
 |
 | #1 x=4.0 L=4.0
 |
 | → -350 ⭯ 0
 |
 | #2 x=8.0 L=4.0
 |
◯| → 0 ⭯ -100
 |
 | #3 x=12.0 L=4.0
 |
◯| → 0 ⭯ 0
 |
 | #4 x=16.0 L=4.0
 |
 | → -200 ⭯ 0
```

For reference, here's the diagram again with my 0-based indices:

![](https://i.imgur.com/rZ0rYBe.png)
![](https://i.imgur.com/VBblIGA.png)

Calling the `beam.solve()` method will print all the values required by the assignment:

```
k_0 =
(indices: 0, 1, 2, 3)
[[ 14062.5  28125.  -14062.5  28125. ]
 [ 28125.   75000.  -28125.   37500. ]
 [-14062.5 -28125.   14062.5 -28125. ]
 [ 28125.   37500.  -28125.   75000. ]]

k_1 =
(indices: 2, 3, 4, 5)
[[ 14062.5  28125.  -14062.5  28125. ]
 [ 28125.   75000.  -28125.   37500. ]
 [-14062.5 -28125.   14062.5 -28125. ]
 [ 28125.   37500.  -28125.   75000. ]]

k_2 =
(indices: 4, 5, 6, 7)
[[ 14062.5  28125.  -14062.5  28125. ]
 [ 28125.   75000.  -28125.   37500. ]
 [-14062.5 -28125.   14062.5 -28125. ]
 [ 28125.   37500.  -28125.   75000. ]]

k_3 =
(indices: 6, 7, 8, 9)
[[ 14062.5  28125.  -14062.5  28125. ]
 [ 28125.   75000.  -28125.   37500. ]
 [-14062.5 -28125.   14062.5 -28125. ]
 [ 28125.   37500.  -28125.   75000. ]]

k_4 =
(indices: 8, 9, 10, 11)
[[ 14062.5  28125.  -14062.5  28125. ]
 [ 28125.   75000.  -28125.   37500. ]
 [-14062.5 -28125.   14062.5 -28125. ]
 [ 28125.   37500.  -28125.   75000. ]]

s =
(indices: 3, 4, 5, 7, 9, 10, 11)
[[150000.  -28125.   37500.       0.       0.       0.       0. ]
 [-28125.   28125.       0.   28125.       0.       0.       0. ]
 [ 37500.       0.  150000.   37500.       0.       0.       0. ]
 [     0.   28125.   37500.  150000.   37500.       0.       0. ]
 [     0.       0.       0.   37500.  150000.  -28125.   37500. ]
 [     0.       0.       0.       0.  -28125.   14062.5 -28125. ]
 [     0.       0.       0.       0.   37500.  -28125.   75000. ]]

P =
(indices: 3, 4, 5, 7, 9, 10, 11)
[[ 100]
 [-350]
 [   0]
 [-100]
 [   0]
 [-200]
 [   0]]

d =
(indices: 3, 4, 5, 7, 9, 10, 11)
[[-0.00349425]
 [-0.02357088]
 [-0.00103448]
 [ 0.00763218]
 [-0.01448276]
 [-0.11481992]
 [-0.03581609]]

u_0 =
(indices: 0, 1, 2, 3)
[[ 0.        ]
 [ 0.        ]
 [ 0.        ]
 [-0.00349425]]

u_1 =
(indices: 2, 3, 4, 5)
[[ 0.        ]
 [-0.00349425]
 [-0.02357088]
 [-0.00103448]]

u_2 =
(indices: 4, 5, 6, 7)
[[-0.02357088]
 [-0.00103448]
 [ 0.        ]
 [ 0.00763218]]

u_3 =
(indices: 6, 7, 8, 9)
[[ 0.        ]
 [ 0.00763218]
 [ 0.        ]
 [-0.01448276]]

u_4 =
(indices: 8, 9, 10, 11)
[[ 0.        ]
 [-0.01448276]
 [-0.11481992]
 [-0.03581609]]

Q_0 =
(indices: 0, 1, 2, 3)
[[ -98.27586207]
 [-131.03448276]
 [  98.27586207]
 [-262.06896552]]

Q_1 =
(indices: 2, 3, 4, 5)
[[ 204.09482759]
 [ 362.06896552]
 [-204.09482759]
 [ 454.31034483]]

Q_2 =
(indices: 4, 5, 6, 7)
[[-145.90517241]
 [-454.31034483]
 [ 145.90517241]
 [-129.31034483]]

Q_3 =
(indices: 6, 7, 8, 9)
[[-192.67241379]
 [  29.31034483]
 [ 192.67241379]
 [-800.        ]]

Q_4 =
(indices: 8, 9, 10, 11)
[[ 2.00000000e+02]
 [ 8.00000000e+02]
 [-2.00000000e+02]
 [-4.54747351e-13]]

R =
(indices: 0, 1, 2, 6, 8)
[[ -98.27586207]
 [-131.03448276]
 [ 302.37068966]
 [ -46.76724138]
 [ 392.67241379]]
```

I have also printed the associate indices for all the matrices. Interpreting them is straightforwards. For column vectors, the indices map to the rows, going down:

![](https://i.imgur.com/KarLG0bm.png)

A similar logic holds for matrices:

![](https://i.imgur.com/o1M9bDD.png)

## How the Algorithm Works

1. Declare material properties, external forces and moments, supports, and the length of the beam.
2. Collect points of interest for the beam which includes $x = 0$, $x = L$, positions of supports, and positions of externals.
3. De-duplicate the points of interest (only keep unique ones) and sort them into a list of $x$ values called the break points.
4. Create members from the break points with joints to the left of the individual members, encoding the moments and forces at the joints.
5. Donate the left joints to the right joint of the previous member for all members except the first one.
6. Compute the stiffness matrix $K$ for all members.
7. Pad the stiffness matrix $K$ for all members so that all members have matrices of the same dimensions with their respective values at the correct indices.
8. Add all stiffness matrices into a global stiffness matrix $s$.
9. Sum all external forces and moments on all joints.
10. Arrange all external forces and moments into a column vector $P_i$.
11. Pad the external forces and moments for all members so that all members have vectors of the same dimensions with their respective values at the correct indices.
12. Sum all the padded external forces and moments into a column vector $P$.
13. Trim the global stiffness matrix $s$ and $P$ to only include the free indices.
14. Solve for $d$.
15. Re-pad $d$ to include $0$ for the fixed indices and pass it back to all the members.
16. Let each member compute its $u$ vector as a subsection of the newly padded $d$ vector.
17. Compute $Q$ for each member.
18. Pad $Q$ for each member so that all members have matrices of the same dimensions with their respective values at the correct indices.
19. Add all padded $Q$ matrices into a global $R$ matrix.
20. Trim the $R$ matrix to only include the fixed indices since the free indices cannot have reaction forces.

## Benchmarks

I used the in-class examples as benchmarks for developing the code. Below are the beams that I used.

## Lecture Example 1

![](https://i.imgur.com/pd6evYs.png)
![](https://i.imgur.com/6k9kQMj.png)

```py
lecture_example_1 = Beam(
    200 * 10**6,
    700 * 10**-6,
    8 + 4,
    [
        Support(0, SupportType.FIXED),
        Support(8, SupportType.ROLLER),
    ],
    [
        External(8 + 4, ExternalType.FORCE, -85),
    ],
)
lecture_example_1.render()
lecture_example_1.solve()
```

```
░░ → 0 ⭯ 0
 |
 | #0 x=0 L=8
 |
◯| → 0 ⭯ 0
 |
 | #1 x=8 L=4
 |
 | → -85 ⭯ 0

k_0 =
(indices: 0, 1, 2, 3)
[[  3281.25  13125.    -3281.25  13125.  ]
 [ 13125.    70000.   -13125.    35000.  ]
 [ -3281.25 -13125.     3281.25 -13125.  ]
 [ 13125.    35000.   -13125.    70000.  ]]

k_1 =
(indices: 2, 3, 4, 5)
[[ 26250.  52500. -26250.  52500.]
 [ 52500. 140000. -52500.  70000.]
 [-26250. -52500.  26250. -52500.]
 [ 52500.  70000. -52500. 140000.]]

s =
(indices: 3, 4, 5)
[[210000. -52500.  70000.]
 [-52500.  26250. -52500.]
 [ 70000. -52500. 140000.]]

P =
(indices: 3, 4, 5)
[[  0]
 [-85]
 [  0]]

d =
(indices: 3, 4, 5)
[[-0.00485714]
 [-0.03238095]
 [-0.00971429]]

u_0 =
(indices: 0, 1, 2, 3)
[[ 0.        ]
 [ 0.        ]
 [ 0.        ]
 [-0.00485714]]

u_1 =
(indices: 2, 3, 4, 5)
[[ 0.        ]
 [-0.00485714]
 [-0.03238095]
 [-0.00971429]]

Q_0 =
(indices: 0, 1, 2, 3)
[[ -63.75]
 [-170.  ]
 [  63.75]
 [-340.  ]]

Q_1 =
(indices: 2, 3, 4, 5)
[[ 8.50000000e+01]
 [ 3.40000000e+02]
 [-8.50000000e+01]
 [ 2.27373675e-13]]

R =
(indices: 0, 1, 2)
[[ -63.75]
 [-170.  ]
 [ 148.75]]
```

## Lecture Example 2

![](https://i.imgur.com/IWbchyz.png)
![](https://i.imgur.com/EzHI8cI.png)

```py
lecture_example_2 = Beam(
    29000 * 10**3,
    310,
    (40 + 60) * 12,
    [
        Support(0, SupportType.FIXED),
        Support((40 + 60) * 12, SupportType.FIXED),
    ],
    [
        External(40 * 12, ExternalType.FORCE, -1000),
        External(40 * 12, ExternalType.MOMENT, -15000),
    ],
)
lecture_example_2.render()
lecture_example_2.solve()
```

```
░░ → 0 ⭯ 0
 |
 | #0 x=0 L=480
 |
 | → -1000 ⭯ -15000
 |
 | #1 x=480 L=720
 |
░░ → 0 ⭯ 0

k_0 =
(indices: 0, 1, 2, 3)
[[ 9.75477431e+02  2.34114583e+05 -9.75477431e+02  2.34114583e+05]
 [ 2.34114583e+05  7.49166667e+07 -2.34114583e+05  3.74583333e+07]
 [-9.75477431e+02 -2.34114583e+05  9.75477431e+02 -2.34114583e+05]
 [ 2.34114583e+05  3.74583333e+07 -2.34114583e+05  7.49166667e+07]]

k_1 =
(indices: 2, 3, 4, 5)
[[ 2.89030350e+02  1.04050926e+05 -2.89030350e+02  1.04050926e+05]
 [ 1.04050926e+05  4.99444444e+07 -1.04050926e+05  2.49722222e+07]
 [-2.89030350e+02 -1.04050926e+05  2.89030350e+02 -1.04050926e+05]
 [ 1.04050926e+05  2.49722222e+07 -1.04050926e+05  4.99444444e+07]]

s =
(indices: 2, 3)
[[ 1.26450778e+03 -1.30063657e+05]
 [-1.30063657e+05  1.24861111e+08]]

P =
(indices: 2, 3)
[[ -1000]
 [-15000]]

d =
(indices: 2, 3)
[[-0.89955951]
 [-0.00105717]]

u_0 =
(indices: 0, 1, 2, 3)
[[ 0.        ]
 [ 0.        ]
 [-0.89955951]
 [-0.00105717]]

u_1 =
(indices: 2, 3, 4, 5)
[[-0.89955951]
 [-0.00105717]
 [ 0.        ]
 [ 0.        ]]

Q_0 =
(indices: 0, 1, 2, 3)
[[   630.]
 [171000.]
 [  -630.]
 [131400.]]

Q_1 =
(indices: 2, 3, 4, 5)
[[   -370.]
 [-146400.]
 [    370.]
 [-120000.]]

R =
(indices: 0, 1, 4, 5)
[[    630.]
 [ 171000.]
 [    370.]
 [-120000.]]
```

## Lecture Example 3

![](https://i.imgur.com/1gmhlKl.png)
![](https://i.imgur.com/jCYzixq.png)

```py
lecture_example_3 = Beam(
    29000 * 10**3,
    310,
    (40 + 60) * 12,
    [
        Support(0, SupportType.FIXED),
        Support((40 + 60) * 12, SupportType.FIXED),
    ],
    [
        External(40 * 12, ExternalType.FORCE, -1000),
        External(40 * 12, ExternalType.MOMENT, -15000),
        External((40 + 60 - 30) * 12, ExternalType.FORCE, -1000),
    ],
)
lecture_example_3.render()
lecture_example_3.solve()
```

```
░░ → 0 ⭯ 0
 |
 | #0 x=0 L=480
 |
 | → -1000 ⭯ -15000
 |
 | #1 x=480 L=360
 |
 | → -1000 ⭯ 0
 |
 | #2 x=840 L=360
 |
░░ → 0 ⭯ 0

k_0 =
(indices: 0, 1, 2, 3)
[[ 9.75477431e+02  2.34114583e+05 -9.75477431e+02  2.34114583e+05]
 [ 2.34114583e+05  7.49166667e+07 -2.34114583e+05  3.74583333e+07]
 [-9.75477431e+02 -2.34114583e+05  9.75477431e+02 -2.34114583e+05]
 [ 2.34114583e+05  3.74583333e+07 -2.34114583e+05  7.49166667e+07]]

k_1 =
(indices: 2, 3, 4, 5)
[[ 2.31224280e+03  4.16203704e+05 -2.31224280e+03  4.16203704e+05]
 [ 4.16203704e+05  9.98888889e+07 -4.16203704e+05  4.99444444e+07]
 [-2.31224280e+03 -4.16203704e+05  2.31224280e+03 -4.16203704e+05]
 [ 4.16203704e+05  4.99444444e+07 -4.16203704e+05  9.98888889e+07]]

k_2 =
(indices: 4, 5, 6, 7)
[[ 2.31224280e+03  4.16203704e+05 -2.31224280e+03  4.16203704e+05]
 [ 4.16203704e+05  9.98888889e+07 -4.16203704e+05  4.99444444e+07]
 [-2.31224280e+03 -4.16203704e+05  2.31224280e+03 -4.16203704e+05]
 [ 4.16203704e+05  4.99444444e+07 -4.16203704e+05  9.98888889e+07]]

s =
(indices: 2, 3, 4, 5)
[[ 3.28772023e+03  1.82089120e+05 -2.31224280e+03  4.16203704e+05]
 [ 1.82089120e+05  1.74805556e+08 -4.16203704e+05  4.99444444e+07]
 [-2.31224280e+03 -4.16203704e+05  4.62448560e+03  0.00000000e+00]
 [ 4.16203704e+05  4.99444444e+07  0.00000000e+00  1.99777778e+08]]

P =
(indices: 2, 3, 4, 5)
[[ -1000]
 [-15000]
 [ -1000]
 [     0]]

d =
(indices: 2, 3, 4, 5)
[[-1.42545584]
 [-0.00232578]
 [-1.13828877]
 [ 0.00355115]]

u_0 =
(indices: 0, 1, 2, 3)
[[ 0.        ]
 [ 0.        ]
 [-1.42545584]
 [-0.00232578]]

u_1 =
(indices: 2, 3, 4, 5)
[[-1.42545584]
 [-0.00232578]
 [-1.13828877]
 [ 0.00355115]]

u_2 =
(indices: 4, 5, 6, 7)
[[-1.13828877]
 [ 0.00355115]
 [ 0.        ]
 [ 0.        ]]

Q_0 =
(indices: 0, 1, 2, 3)
[[   846.]
 [246600.]
 [  -846.]
 [159480.]]

Q_1 =
(indices: 2, 3, 4, 5)
[[-1.5400e+02]
 [-1.7448e+05]
 [ 1.5400e+02]
 [ 1.1904e+05]]

Q_2 =
(indices: 4, 5, 6, 7)
[[  -1154.]
 [-119040.]
 [   1154.]
 [-296400.]]

R =
(indices: 0, 1, 6, 7)
[[    846.]
 [ 246600.]
 [   1154.]
 [-296400.]]
```
