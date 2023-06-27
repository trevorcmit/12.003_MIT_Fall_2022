%% budyko_solver.m
% plot y_i and T_p as functions of fractional change in solar forcing 
% for the Budyko-type EBM with linear radiative heat loss and step-function
% albedo in temperature
%
% outline:
% -define parameters
% -define arrays for key variables
% -calculate insolation as a function of sine of latitude
% -calculate radiative forcing needed to sustain ice edge 
%     at a given latitude for partially ice-covered climate 
% -calculate stability of partially ice-covered climate states 
% -calculate minimum radiative flux to keep ice-free climate and maximum for snowball
% -plot results (making nice plots takes up much of the code) 
%
% Written by Tim Cronin, twcronin@mit.edu, 8/27-8/28/2018
% Modified to change from change in solar brightness to uniform radiative
% forcing 9/29-9/30/2022
%
% debugged/tested by: {XX}

% parameters
%name           value       units           comments
%--------------------------------------------------------------------------------------
A       =       -353;       % W/m^2         OLR intercept
B       =       2.00;       % W/m^2/K       OLR slope / radiative damping coefficient
D       =       3.8;        % W/m^2/K       climate heat transport coefficient; Roughly Budyko's \beta converted to SI
D_ref   =       3.8;        % W/m^2/K       reference value of heat transport coefficient
alpha_0 =       0.3;        % -             albedo when ice-free
alpha_2 =       0.1;        % -             second legendre polynomial coefficient for latitudinal dependence on albedo under ice-free conditions    
dalpha  =       0.22;       % -             increase in albedo when ice-covered
Tf      =       273.15;     % K             temperature threshold for ice
S0      =       1360;       % W/m^2         solar constant, perpendicular incidence
s2      =       -0.48;      % -             second legendre polynomial coefficient for insolation (normalized)  

yi      = (0:0.001:1);      % sine-latitude of ice edge
F_yi    = zeros(size(yi));  % decrease in A required to maintain ice line at yi
ASR_yi  = zeros(size(yi));  % solar absorption with ice-line at yi for reference S0
Tp_yi   = zeros(size(yi));  % global-mean temperature with ice line at yi
Tp0_yi  = zeros(size(yi));  % global-mean temperature with ice line at yi and F=0

insol   = S0/4*(1+s2*0.5*(3*yi.^2-1));           % annual-mean insolation as a function of latitude
alpha_warm = alpha_0 + alpha_2*0.5*(3*yi.^2-1);  % ice-free albedo
alpha_cold = alpha_warm + dalpha;                % ice-covered albedo 

% for each latitude, calculate ASR(y_i), F(y_i), and T_p(y_i)
for j=1:length(yi)
    ASR_yi(j) = yi(j)*mean(insol(1:j).*(1-alpha_warm(1:j))) + ...
        (1-yi(j))*mean(insol(j:end).*(1-alpha_cold(j:end))); 
    % global-mean absorbed solar radiation with ice line at yi

    Tp0_yi(j) = 1/B*(ASR_yi(j) - A);
    
    num = -(insol(j)*(1-(alpha_warm(j)+alpha_cold(j))/2) - (A + B*Tf) + D.*(Tp0_yi(j)-Tf));
    denom = 1+D/B;
    
    F_yi(j) = num/denom;
    
    % radiative forcing required to keep partly ice-covered
    % climate with ice line at yi
    
    Tp_yi(j)   = 1/B*(ASR_yi(j) - A + F_yi(j));
    % global-mean temperature for partly ice-covered
    % climate with ice line at yi
end

% calculate minimum possible radiative forcing that will keep climate ice-free
% by setting polar T equal to Tf and using alpha_warm everywhere
F_min_icefree = -(insol(end)*(1-(alpha_warm(end))) - (A + B*Tf) + D.*(Tp0_yi(end)-Tf))/(1+D/B);

% then calculate maximum possible solar forcing that will allow a snowball
% climate by setting equatorial T equal to Tf and using alpha_cold everywhere
F_max_snowball = -(insol(1)*(1-(alpha_cold(1))) - (A + B*Tf) + D.*(Tp0_yi(1)-Tf))/(1+D/B);

%del_max_snowball = (A*(1+D/B) + Tm*(B+D))/...
%    (insol(1)*(1-alpha_i) + D*ASR_yi(1)/B)  - 1;

% The stability condition of the Budyko model is that the ice line retreat 
% as the solar forcing increases, so filter
% calculations for that criterion
dyi_dlnS = diff(yi)./diff(F_yi);
dyi_dlnS = [-1 dyi_dlnS]; 
% diff() reduces the array size by 1, so pad with a leading negative value:
% model will always be unstable with the ice edge very close to equator;
% see Roe & Baker (2010), "Notes on a Catastrophe"

%% Make figure
figure('Position',[50 50 500 600]); % bracketed array gives size of figure, in pixels 

% first subplot: y_i against delta
subplot(2,2,1); % set up 2x2 array of subfigures, and select the first (top-left) panel
hold on;
set(gca,'Fontsize',14); % set the font size at 12 pt. YMMV depending on screen size
if sum(dyi_dlnS<0)>0
    plot(F_yi(dyi_dlnS<0), yi(dyi_dlnS<0),':','color',[1 0 0],'LineWidth',1); % unstable branch
end
if sum(dyi_dlnS>0)>0
    plot(F_yi(dyi_dlnS>0), yi(dyi_dlnS>0),'color',[0 0 1],'LineWidth',1.5); % stable branch
end
F_min_plot = min([min(F_yi)-5 F_min_icefree-5]); % calculate minimum value of delta for plot
F_max_plot = max([max(F_yi)+5 F_max_snowball+5]); % and max value of delta for plot
line([F_min_plot F_max_snowball],[0 0],...
    'color',[0 1 1],'LineWidth',1.5); % stable snowball branch
line([F_min_icefree F_max_plot],[1 1],...
    'color',[1 0 1],'LineWidth',1.5); % stable ice-free branch
line([0 0],[0 1],'color','k'); % line crossing equilibria with no solar perturbation
xlim([F_min_plot F_max_plot])
box on;
xlabel('Global radiative forcing, $F=A_0-A$','Interpreter', 'Latex');
ylabel('Ice-line sine latitude, $y_I$','Interpreter', 'Latex');
title('a) Ice line stability diagram', 'Fontweight','normal','Interpreter', 'Latex')

% second subplot: insolation against y
subplot(2,2,2)
hold on;
set(gca,'Fontsize',14);
plot(insol, yi,'color',[0 0 0],'LineWidth',1.5);
box on;
ylabel('sine latitude, $y$','Interpreter', 'Latex');
xlabel('insolation (W/m$^2$)','Interpreter', 'Latex')
title('b) Insolation against latitude', 'Fontweight','normal','Interpreter', 'Latex')

% third subplot: global-mean temperature T_p against delta
subplot(2,2,3)
hold on;
set(gca,'Fontsize',14);
if sum(dyi_dlnS<0)>0
    plot(F_yi(dyi_dlnS<0), Tp_yi(dyi_dlnS<0),':','color',[1 0 0],'LineWidth',1);
end
if sum(dyi_dlnS>0)>0
    plot(F_yi(dyi_dlnS>0), Tp_yi(dyi_dlnS>0),'color',[0 0 1],'LineWidth',1.5);
end
line([F_min_plot F_max_snowball],...
    [(mean(insol.*(1-alpha_cold))-A+F_min_plot)/B ...
    (mean(insol.*(1-alpha_cold))-A+F_max_snowball)/B],...
    'color',[0 1 1],'LineWidth',1.5); % snowball climate branch
line([F_min_icefree F_max_plot],...
    [(mean(insol.*(1-alpha_warm))-A+F_min_icefree)/B ...
    (mean(insol.*(1-alpha_warm))-A+F_max_plot)/B],...
    'color',[1 0 1],'LineWidth',1.5); % ice-free climate branch
Tmax_plot = (mean(insol.*(1-alpha_warm))-A+F_max_plot)/B;
Tmin_plot = (mean(insol.*(1-alpha_cold))-A+F_min_plot)/B;
box on;
xlabel('Global radiative forcing, $F=A_0-A$','Interpreter', 'Latex');
ylabel('global-mean temperature, K','Interpreter', 'Latex');
xlim([F_min_plot F_max_plot]);
ylim([Tmin_plot Tmax_plot]);

line([0 0],[Tmin_plot Tmax_plot],'color','k'); % line crossing equilibria with no radiative forcing
if sum(dyi_dlnS<0)==0
    hl = legend('Stable, partial ice-cover','Snowball','Ice-free');
elseif sum(dyi_dlnS>0)==0
    hl = legend('Unstable, partial ice-cover','Snowball','Ice-free');
else
    hl = legend('Unstable, partial ice-cover','Stable, partial ice-cover','Snowball','Ice-free');
end

set(hl,'Position',[0.5050    0.3567    0.3360    0.0958]);
title('c) $\overline{T}$ stability diagram', 'Fontweight','normal', 'Interpreter', 'Latex')

gcfsavepdf('/Users/timothycronin/Dropbox/Teaching/12.003_F22/Notes/Lesson10_AlbedoFeedback/Fig02_Budyko_diagrams.pdf')

%%
if D==D_ref    
    figure;
    plot(yi,F_yi,'Linewidth',2);
    set(gca,'Fontsize',18);
    line([0 1],[0 0],'color','k');
    xlabel('Sine of ice-line latitude, y_I');
    ylabel('Radiative forcing F(y_I), W/m^2');
    title('Solutions for F(y_I) with partial ice cover','Fontweight','normal')
    gcfsavepdf('/Users/timothycronin/Dropbox/Teaching/12.003_F22/Notes/Lesson10_AlbedoFeedback/Fig01_F_yI_ref.pdf')
end




%% 
% also calculate T(y) for F=0 with partial ice cover if such a solution exists
yice = interp1(F_yi(dyi_dlnS>0),yi(dyi_dlnS>0),0);
Tbar = interp1(F_yi(dyi_dlnS>0),Tp_yi(dyi_dlnS>0),0); % interpolate to find global-
% mean temperature and ice-line latitude
T_F0 = (((yi<=yice).*(1-alpha_warm)+(yi>yice).*(1-alpha_cold)).*insol - A + 
D*Tbar)/(B+D);
% temperature as a function of latitude in partial ice-cover solution
% temperature as a function of latitude for ice-free solution (if it exists
% at F=0)
if F_min_icefree<0
    yice = 1;
    Tbar = (mean(insol.*(1-alpha_warm))-A)/B;
    T_F0_icefree = (((yi<=yice).*(1-alpha_warm)+(yi>yice).*(1-alpha_cold)).*insol -
A + D*Tbar)/(B+D);
end
% temperature as a function of latitude for snowball solution (if it exists
% at F=0)
if F_max_snowball>0
    yice = 0;
    Tbar = (mean(insol.*(1-alpha_cold))-A)/B;
    T_F0_snowball = (((yi<yice).*(1-alpha_warm)+(yi>=yice).*(1-alpha_cold)).*insol 
- A + D*Tbar)/(B+D);
end
% figure;
% plot(T_F0, yi)
% hold on;
