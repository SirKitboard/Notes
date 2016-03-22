#!/usr/bin/env perl

use strict;
use warnings;

open FILES, "< ".$ARGV[0] or die "Cant open input file";

while(<FILES>) {
    #Test if file exists
    chomp $_;
    if(-e $_) {
        print "E  ";

        #if exists, test everything else
        if(-t $_) {
            print "T  ";
        } else {
            print "-  ";
        }

        if(-r $_) {
            print "R  ";
        } else {
            print "-  ";
        }

        if(-w $_) {
            print "W  ";
        } else {
            print "-  ";
        }

        if(-x $_) {
            print "X  ";
        } else {
            print "-  ";
        }
    } else {
        #If file doesnt exist, we can assume remaining properties to be false
        print "-  -  -  -  -  ";
    }

    print $_ . "\n";
}
