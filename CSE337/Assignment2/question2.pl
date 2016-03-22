#!/usr/bin/perl

# perl -le "print ((map{('\!', '?', '#', ';', '-')[rand 5]} 1..2), (map{('a'..'z', 'A'..'Z')[rand 42]} 1..4), (map{('0'..'9')[rand 10]} 1..2))"

# print join " # ", grep{$_ % 3 == 0} split / /, "1 3 4 5 6 7 8 9";
# print join "", grep{/[0-9]/} split //, "CSE337";
# print "\n";
# print grep{$_ }

use List::Util "reduce";

# print 2 % 2 == 0;
print reduce {(($a % 2 eq 0) ? $a : $a) + (($b % 2 eq 0) ? $b / 2 : $b)} 0, 1..100;
print "\n";
# print reduce { $a + $b } 1 .. 10
