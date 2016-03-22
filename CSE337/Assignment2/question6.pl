use strict;
use warnings;

#Open input
open HTML , "< ".$ARGV[0] or die "Cant open input file";

#Open output file
open OUTPUTHTML, "> images.html" or die "Cant open output file";

#Print html tags
print OUTPUTHTML "<html>\n";
print OUTPUTHTML "<title>337 A2 HTML images</title>\n";
print OUTPUTHTML "<body>\n";
while(<HTML>) {
    #If regex doesn't match, continue loop
    next unless /data-imageurl=\"(http:\/\/[34][0-9].*\.jpg)\"/;

    #else print image
    print OUTPUTHTML "<img src=\"$1\"/>\n";
}

#close html
print OUTPUTHTML "</body>";
print OUTPUTHTML "</html>";
