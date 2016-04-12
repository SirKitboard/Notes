use strict;
use warnings;

open INPUT , "< ".$ARGV[0] or die "Cant open input file";

while(<INPUT>) {
    # chomp $_;
    # if(//)
    s/\b([0-9]{2}\/[0-9]{2})\/([5-9][0-9])\b/$1\/19$2/g;
    s/\b([0-9]{2}\/[0-9]{2})\/([0-4][0-9])\b/$1\/20$2/g;
    print($_);
}
