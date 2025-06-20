#!/usr/bin/perl
use strict;
use warnings;
use JSON;

my $data = { message => "Hello, World!" };
print encode_json($data) . "\n";
