fun member(e,l) = if l=[] then false else if e=hd(l) then true else member(e,tl(l));
