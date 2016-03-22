use strict;
use warnings;

my $numKeys = keys %ENV;

print "Number of variables in PATH : " . $numKeys . "\n\n";

my $pathDirs = $ENV{PATH};

print "Content of PATH : " . $pathDirs . "\n\n";

print "Number of directories in path : " . split(/:/, $pathDirs) , "\n\n";

print "Sorted directories : \n";
print join("\n", split /:/, $pathDirs) . "\n\n";

#Adding current directory to path
$ENV{PATH} = $ENV{PATH} . ":.";
print "Executing 'while.pl' : \n\n";
system("while.pl");
