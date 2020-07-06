load sunspot.dat  %IMPORTO DATOS cualquiera
year = sunspot(:,1);  
relNums = sunspot(:,2); 

findpeaks(relNums,year) %ENCUENTRO PEAKS
xlabel('Year')
ylabel('Sunspot Number') 
title('Find All Peaks')

%%
findpeaks(relNums,year,'MinPeakProminence',40) %filtro mejor los peaks
%ejemplos:
%NPeaks: numero maximo de picos

%SortStr: ascend o descen

%MinPeakHeight: altura minima

%MinPeakProminence, ve la separacion de pico, distancia minima relativa
%importante (elimina peaks que esten muy cerca del peak relevante) (ver
%bien por que el 40)

%'Threshold' — Diferencia mínima de altura

%'MinPeakDistance' — Separación mínima de picos
xlabel('Year') 
ylabel('Sunspot Number') 
title('Find Prominent Peaks')

%%
figure 
[pks, locs] = findpeaks(relNums,year,'MinPeakProminence',40); %guarda valores de ambos ejes donde estan los peaks
peakInterval = diff(locs); %funcion que calcula la diferencia entre valores seguidos del array
hist(peakInterval) %hago histograma para visualizarlo mejor
grid on
xlabel('Year Intervals')
ylabel('Frequency of Occurrence') 
title('Histogram of Peak Intervals (years)')

%%
AverageDistance_Peaks = mean(diff(locs)) %finalmente sacamos el promedio que es lo que necesitamos


















