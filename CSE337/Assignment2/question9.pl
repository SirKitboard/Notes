use strict;
use warnings;

#Open input
open INPUT , "< ".$ARGV[0] or die "Cant open input file";
my %wordsDict;
my $previousWord;

while(<INPUT>) {
    chomp $_;
    my @words = split / /, $_;
    foreach my $word(@words) {
        if(!$previousWord) {
            $previousWord = $word;
            next;
        }
        if($wordsDict{$previousWord}) {
            # $wordsDict{$previousWord} = ($word => "=");
            if($wordsDict{$previousWord}{$word}) {
                $wordsDict{$previousWord}{$word} = $wordsDict{$previousWord}{$word} . "=";
            } else {
                $wordsDict{$previousWord}{$word} = "=";
            }
        } else {
            $wordsDict{$previousWord} = {$word => "="};
        }
        $previousWord = $word;
    }

}

print "Enter a word : ";
my $inputWord = <STDIN>;
chomp $inputWord;
if($wordsDict{$inputWord}) {
    while(my ($key, $value) = each(%{$wordsDict{$inputWord}})) {
        print $key . "\t" . $value . "\n";
    }
} else {
    print "Word not found";
}
