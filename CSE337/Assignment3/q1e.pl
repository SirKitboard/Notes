use strict;
use warnings;

print "input pattern : ";
my $pattern = <STDIN>;
chomp $pattern;

print "input string : ";
while(<STDIN>) {
    chomp $_;
    if(/$pattern/) {
        s/($pattern)/<$1>/;
        print($_);
    } else {
        print "no match";
    }
    print "\ninput string : ";
}
