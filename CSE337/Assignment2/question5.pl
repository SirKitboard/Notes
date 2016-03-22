use strict;
use warnings;

my $input = "pda lupdkj lnkcnwiiejc hwjcqwca swo ejrajpaz xu cqezk rwj nkooqi, w zqpydykilqpan lnkcnwiian, wxkqp 25 uawno wck. rwj nkooqi zabejaz deo ckwho bknlupdkj wo bkhhkso: wj awou wjz ejpqepera hwjcqwca fqop wo lksanbqh wo iwfknykilapepkno; klaj okqnya, ok wjukja ywj ykjpnexqpa pk epo zarahkliajp; ykzapdwp eo wo qjzanopwjzwxha wo lhwej ajcheod; oqepwxehepu bkn aranuzwu pwogo,whhksejc bkn odknp zarahkliajp peiao";

my $decryptChar = sub {
    # print shift;
    my $charIndex = ord(shift);
    # print(chr($charIndex));
    if($charIndex >= 65 && $charIndex <= 90) {
        my $newIndex = ($charIndex - 61) % 26 + 65;
        return chr($newIndex);
    } elsif($charIndex >= 97 && $charIndex <= 122) {
        my $newIndex = ($charIndex - 93) % 26 + 97;
        return chr($newIndex);
    } else {

        return chr($charIndex);
    }
};

my $encryptText = sub {
    my $charIndex = ord(shift);

    if($charIndex >= 65 && $charIndex <= 90) {
        my $newIndex = ($charIndex - 69) % 26 + 65;
        return chr($newIndex);
    } elsif($charIndex >= 97 && $charIndex <= 122) {
        my $newIndex = ($charIndex - 101) % 26 + 97;
        return chr($newIndex);
    } else {
        # print "hi\n";
        return chr($charIndex);
    }
};

print "Input string : " . $input . "\n\n";
my @decryptedText = map{$decryptChar->($_)} split('', $input);

print "Decrypted Text : " . join('', @decryptedText) . "\n\n";

print "Recrypted Text : ";
print map{$encryptText->($_)} @decryptedText;
print "\n\n"
