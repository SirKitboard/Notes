$num = 5;
$num = $ARGV[0] if $ARGV[0];
$numCorrect = 0;
do {
    # print int(rand 20)+1 . " " . ((int(rand 2) + 1) == 1 ? ') . " " . int(rand 30) . " = ";
    $num = $num - 1;
} until($num eq 0)
