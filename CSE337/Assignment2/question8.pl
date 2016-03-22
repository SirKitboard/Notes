use strict;
use warnings;

#Open input
open INPUT , "< ".$ARGV[0] or die "Cant open input file";
my %wordsDict;

while(<INPUT>) {
    chomp $_;
    my @words = split / /, $_;
    # print @words;
    foreach my $word(@words) {
        if($wordsDict{$word}) {
            $wordsDict{$word} = $wordsDict{$word} . "=";
        } else {
            $wordsDict{$word} = "=";
        }
    }
}

print "Words hash : \n";
while(my ($key, $value) = each(%wordsDict)) {
    print $key . "\t" . $value . "\n";
}
