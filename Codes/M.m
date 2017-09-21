clc;
clear all;

matrix = load('windmachine.csv');
colM = matrix(:,12);
colN = matrix(:,13);

% whole session;
plot(colM, 'b-', xlabel = 'Dot',ylabel = '引风机3B润滑油压力');

% 

