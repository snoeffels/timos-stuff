clear all
close all
clf

x = linspace(390,410,1000);
a = 0.001; b = 0.1; c = 2000; x0p = 400;
x01 = 395; w1 = 1; a1 = 2;
x02 = 405; w2 = 0.5; a2 = 6;

figure(1)
plot(x,full_fit(x,x0p,a,b,c,x01,w1,a1,x02,w2,a2))

figure(2)
plot(x,voigt(x,x01,w1,a1))
countsVoigt1 = sum(voigt(x,x01,w1,a1));



function ret = full_fit(x,x0p,a,b,c,x01,w1,a1,x02,w2,a2)
    ret= polynom(x,x0p,a,b,c) + voigt(x,x01,w1,a1) + voigt(x,x02,w2,a2);
end


function ret = polynom(x,x0,a,b,c)
    ret = a*(x-x0).^2 + b*(x-x0) + c;
end


function ret = voigt(x,x0,w,a)
    ret = a./(1+((x-x0)/w).^2);
end