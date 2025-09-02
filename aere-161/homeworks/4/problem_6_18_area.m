function [area] = problem_6_18_area(x1, y1, x2, y2, x3, y3) % declare function with 6 arguments and 1 return
a = problem_6_18_length(x1, y1, x2, y2); % get side length a
b = problem_6_18_length(x2, y2, x3, y3); % get side length b
c = problem_6_18_length(x3, y3, x1, y1); % get side length c

s = (a + b + c) / 2; % calculate semiperimeter

area = sqrt(s * (s - a) * (s - b) * (s - c)); % calculate area
end % end function