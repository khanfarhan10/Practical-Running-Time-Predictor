function [J , gradient] = computeCost(x , y , theta)
  m = length(y);
  J = (0.5 / m) .* (x * theta - y )' * (x * theta - y );
  gradient = (1/m) .* x' * (x * theta - y);
end