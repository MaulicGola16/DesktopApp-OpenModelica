within NonInteractingTanks;

model Tank2
parameter Real A =1, V =10;
Real h,Q1,T;
  FlowConnect flowConnect annotation(
    Placement(visible = true, transformation(origin = {-42, 42}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {-36, 34}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
Q1 = flowConnect.F;
der(h) = Q1 / A;
T = V/(Q1);
  annotation(
    Icon(graphics = {Line(origin = {-13, 13.5}, points = {{-35, 28.5}, {-35, -31.5}, {33, -31.5}, {35, -31.5}, {35, 26.5}, {35, 28.5}, {35, 24.5}}), Text(lineColor = {0, 0, 255}, extent = {{0, 30}, {50, 80}}, textString = "%name")}));
end Tank2;
