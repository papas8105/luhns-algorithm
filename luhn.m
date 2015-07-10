function luhns_algorithm
c_id  = input('Enter the card number: ');
if isstr(c_id) == 0
    c_id = num2str(c_id);
end
c = cell(1,length(c_id));
for ii = 1 : length(c_id)
    c{ii} = str2num(c_id(ii));
end
odd_index = [];
for ii = 1 : 2 : length(c_id)
    odd_index = [odd_index c{ii}];
end
s1 = sum(odd_index); even_index = [];
for ii = 2:2:length(c_id)
    even_index = [even_index 2*c{ii}];
end
for ii = 1 : length(even_index)
    if even_index(ii)>10
        even_index(ii) = mod(even_index(ii),10) + 1;
    end
end
s2 = sum(even_index); s = s1 + s2;
if mod(s,10)==0
    display(sprintf('The card is valid!\n'));
else
    display(sprintf('The card is invalid!\n'));
end
end
