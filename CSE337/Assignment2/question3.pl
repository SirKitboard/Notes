use strict;
use warnings;

$num = 5;
$num = $ARGV[0] if $ARGV[0];
$totalNum = $num;
$numCorrect = 0;
do {
    # print int(rand 20)+1 . " " . ((int(rand 2) + 1) == 1 ? ') . " " . int(rand 30) . " = ";
    my $a = int(rand 20)+1;
    my $b = int(rand 30)+1;
    my $op = ((int(rand 2) + 1) == 1 ? "+" : "-");\

    print $a . " " . $op . " " . $b . " = ";
    my $inputValue = <STDIN>;
    chomp $inputValue;

    if($op eq "+") {
        if($inputValue eq ($a + $b)) {
            $numCorrect++;
            print "Excellent!\n"
        }
    } else {
        if($inputValue eq ($a - $b)) {
            $numCorrect++;
            print "Excellent!\n"
        }
    }
    print "\n";
    $num = $num - 1;
} until($num eq 0);

print "Your score is " . $numCorrect . " out of " . $totalNum . ". That's " . ($numCorrect * 100 / $totalNum) . "% correct. Congrats\n";
