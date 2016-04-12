use strict;
use warnings;

my $length = $ARGV[0];
my $position1 = $ARGV[1];
my $letter1 = $ARGV[2];
my $position2 = $ARGV[3];
my $letter2 = $ARGV[4];
if($position1 > $length or $position2 > $length) {
    die "Invalid parameters";
}
if($position2 < $position1) {

    # Swap the 2 if second is smaller than first
    my $temp = $position1;
    $position1 = $position2;
    $position2 = $temp;

    $temp = $letter1;
    $letter1 = $letter2;
    $letter2 = $temp;
}

my $indexDifference = $position2 - $position1 - 1;
my $lengthIndexDifference = $length - $position2;
$position1  = $position1 - 1;

my $pattern = ".{$position1}[$letter1].{$indexDifference}[$letter2].{$lengthIndexDifference}";

# print($pattern);
open INPUT , "< /usr/share/dict/words" or die "Cant open input file";

while(<INPUT>) {
    if(/^$pattern$/) {
        print($_);
    }
}
