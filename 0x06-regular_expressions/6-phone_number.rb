#!/usr/bin/env ruby
#A regular expression that matches a 10 digit phone number

puts ARGV[0].scan(/^\S*\d{10,10}/).join
