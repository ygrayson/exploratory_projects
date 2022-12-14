%{
    In this project, we plan to investigate the current situation of 
    COVID-19 using epidemic modeling. We will potentially be doing both 
    model selection and parameter estimation in order to find a good model 
    of the outbreak. One of the models that is worth trying is the SEIR 
    model that we discussed in class. We are looking at some 
    local regions in Michigan and how different regions might have a 
    different model as a good fit. With the existing data in hand, 
    we would hope to generate a good prediction into the future of the 
    outbreak. 

    We're gonna use the model we used for the ebola outbreak to help get
    started with the model.

        S is the number of susceptible people.
        E is the number of exposed people.
        I is the number of infected people.
        R is the number of recovered people.
        y is the number of total case counts for infection.

%}

%Data has three colums (hours, case counts, days)
%There should be a bug somewhere for the time, we should be able to do this
%in days
dataCases = load('covid_data.txt');
days = dataCases(:, 3);
hours = dataCases(:, 1);
case_count = dataCases(:, 2);

%Plot the data.
figure('name', 'SEIR Model with COVID-19 Data');
hold on;
plot(days, case_count, '.');
xlabel('Time (hours)');
ylabel('Total numbers of case counts');
title('Number of case counts as a function of time');

B = 1.4876; %Beta
A = .7238; %Alpha 
r = 1.4701; %Gamma
N = 2000000; %This is the total number of people 

%Define the initial conditions.
I0 = case_count(1) / N;
E0 = 5 * I0;
S0 = 1 - I0 - E0;
R0 = 0;
y0 = N * A * E0;

%Define the vectors for the parameters and initial conditions.
params = [B,A,r,N];
x0 = [S0,E0,I0,R0,y0];
tspan = dataCases(:,1);
tdays = dataCases(:,3);

%Call the function seirode to evaluate the values and then plot the
%ydot solutions vs time.
options = odeset('AbsTol', 1e-8, 'RelTol', 1e-8);
fun = @(t,x) covidseirode(t,x,params);
[~,xsol] = ode45(fun,tspan,x0,options);
plot(tdays,xsol(:,5),'*');

%This portion solves for the Poisson LL to help determine better 
%parameters for the SEIR model to better fit the data.

fun1 = @(v) covidseirPois(v);
v0 = [B,A,r];
%fminsearch helps find the minimal value for the parameters. Which in turns
%optimizes the ODE.
varparsPois = fminsearch(fun1,v0);

%This portion solves for the least squares to help determine better 
%parameters for the SEIR model to better fit the data.

fun2 = @(v) covidseirLS(v);
u0 = [B,A,r];
%fminsearch helps find the minimal value for the parameters. Which in turns
%optimizes the ODE.
varparsLS = fminsearch(fun2,u0);

B = 1.4886; %Beta
A = .9885; %Alpha 
r = 1.4741; %Gamma

params = [B,A,r,N];
x0 = [S0,E0,I0,R0,y0];

options = odeset('AbsTol',1e-8,'RelTol',1e-8);
fun = @(t,x) covidseirode(t,x,params);
[t,xsol] = ode45(fun,tspan,x0,options);
plot(tdays,xsol(:,5),'x');
saveas(gcf, "./plots/optimal_params.jpg");


%Average cost of hospitalization of a respiratory system diagnosis with 
%ventilator support for more than 96 hours is $40,128. For less severe
%cases, the total cost will be on average $13,297. 

%About 15% of the people that are infected will need to be hospitalized.

%About 15% of the people that will be hospitalized are expected to be 
%in serious care. 

%And about 2 to 7% of people who will be hospitalized will be uninsured. So
%we are going approximate it by 5.5%

%Detroit has 4,123 hospital beds and 509 ICU beds and Michigan as a state
%has 2000 ventilators

%We should model the amount of hospital beds and ventilators that the
%county has and do a "birth death" system to show more of an accurate cost
%model for the SEIR model we have made.

seriousCareCost = 40128;
regularCareCost = 13297;
lastDay = dataCases(end,3);

totalCostPerDay = zeros(lastDay-1,1);
ydot = zeros(lastDay - 1,1);

for ii = 1:(lastDay - 1)
    ydot(ii) = xsol(ii+1,5) - xsol(ii,5);
    hospitalizedPeople = ceil(.15.*ydot(ii));
    uninsuredPeople = ceil(.05.*hospitalizedPeople);
    seriousCarePeople = ceil(.15.*uninsuredPeople);
    regularCarePeople = uninsuredPeople - seriousCarePeople;
    
    %Here is the total cost to the government fro the day
    totalCostPerDay(ii) = seriousCareCost.*seriousCarePeople + regularCarePeople.*regularCareCost;
end

figure;
days = 1:dataCases(end - 1,3);
bar(days,totalCostPerDay(:));
ylim([0 225000]);
saveas(gcf, './plots/costs.jpg');
%{
B = varpars(1);
A = varpars(2);
r = varpars(3);
params = [B,A,r];

tspan = dataCases(:,1);
options = odeset('AbsTol',1e-8,'RelTol',1e-8);
fun = @(t,x) covidseirode(t,x,params);
[t,xsol] = ode45(fun,tspan,x0,options);
plot(tspan,xsol(:,5),'*');
%}
