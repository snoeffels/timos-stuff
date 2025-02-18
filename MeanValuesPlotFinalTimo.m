clear all
close all
clc

% Verzeichnis, in dem sich die ASCII-Dateien befinden
location = "\\Eve\sharepretzler\Timo Wenier\20240927\MatlabAlZ500";

%Dateien im Ordner auflisten
files = dir(location);
files = files(~ismember({files.name},{'.' , '..'}));
numFiles = length(files);

%in drei Gruppen einteilen
group1 = files(1:3:end);    % Gruppe 1
group2 = files(2:3:end);    % Gruppe 2
group3 = files(3:3:end);    % Gruppe 3

%Arrays zum speichern erstellen
empty1 = zeros(1024 , 1);
empty2 = zeros(1024 , 1);
empty3 = zeros(1024 , 1);

%Schleife zum aufaddieren der Gruppe 1
for i = 1:length(group1)
    file = location + '\' + group1(i).name;
    data = load(file);
    empty1 = empty1 + data(: , 2);
end
meanValues1 = empty1/length(group1); %Vektor mit den gemittelten Counts

wavelength = data(: , 1); %Vektor mit allen Wellenlängen

final1 = [wavelength , meanValues1]; 

%Schleife zum aufaddieren der Gruppe 2
for i = 1:length(group2)
    file = location + '\' + group2(i).name;
    data = load(file);
    empty2 = empty2 + data(: , 2);
end
meanValues2 = empty2/length(group2); %Vektor mit den gemittelten Counts

wavelength = data(: , 1); %Vektor mit allen Wellenlängen

final2 = [wavelength , meanValues2]; 

%Schleife zum aufaddieren der Gruppe 3
for i = 1:length(group3)
    file = location + '\' + group3(i).name;
    data = load(file);
    empty3 = empty3 + data(: , 2);
end
meanValues3 = empty3/length(group3); %Vektor mit den gemittelten Counts

wavelength = data(: , 1); %Vektor mit allen Wellenlängen

final3 = [wavelength , meanValues3]; 

plot(final1(:,1) , final1(:,2) , 'b');

hold on

plot(final2(:,1) , final2(:,2) , 'r');

hold on

plot(final3(:,1) , final3(:,2) , 'g');

%Legende erstellen
legend('1st shot' , '2nd shot' , '3rd shot');

% Achsenbeschriftungen hinzufügen
xlabel('x-Achse (Wellenlänge in nm)');  % Beschriftung der x-Achse
ylabel('y-Achse (Counts)');          % Beschriftung der y-Achse

% Optional: Titel hinzufügen
title('Gemittelte Counts für Z=500');

hold off