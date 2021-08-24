clc;
clear;
clear all;

%(-inf) = This will indicating the Walls in the Rooms/No access to traverse inbetween

Ag = [-inf,0,-inf,0,-inf,-inf,-inf;
 0,-inf,0,0,0,-inf,-inf;
 -inf,0,-inf,-inf,-inf,0,100;
 0,0,-inf,-inf,-inf,-inf,100;
  -inf,0, -inf,-inf,-inf,0,-inf;
 -inf,-inf,0,-inf,0,-inf,-inf;
 -inf,-inf,0,0,-inf,-inf,100;]

Gstat = 7; %Destined room for agent to traverse
gamma = 0.8; %Initializing the learning rate
qMat= zeros(size(Ag)); % Initializing the Qmatrix for the Learning

for episode = 1:1000 %Number of iterations to be Performed
  %Initial state selection Ranomly to Start the Procedure
  z = randperm(size(Ag,1));
  statement = z(1);
  
  while statement ~= Gstat
    %Let's Find the all possiable combinations of Epsiodes
    Epsiodes = find(Ag(statement,:) >=0);
    if size(Epsiodes, 2) > 0
      %Randomly Picking a one Episode to Start
      j = randperm(size(Epsiodes, 2));
      Epsiode = Epsiodes(j(1));
    end
     
     %Compute a Vector coulmn
     qMaximum = max(qMat, [], 2); % Provides the Maximum value for Subsequnt rows 
     
     %Coulmn Basis
     %Finding the qMat with variables
     qMat(statement, Epsiode) = Ag(statement,Epsiode ) + gamma*qMaximum(Epsiode);
     %Moving to the Next Statement
     statement = Epsiode ; #in Here episode means action 
     
  end
end

p = max(max(qMat));
qMat = qMat/p*100 #Doing the Qmatrix Normalization


statement=1; %Starting Room 

printf("Traversal Order for Agent \n");
display(statement); #Rooms numbered according to 1-7. (To get actual room No)
while statement~=Gstat
  [mx,Epsiode] =max(qMat(statement,:));   # Selecting the Maximum Values for the Traversal
  statement =Epsiode ;
  display(statement)
 
end
printf("Agent Reached the Destination \n");