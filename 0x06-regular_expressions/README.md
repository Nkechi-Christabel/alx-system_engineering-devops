<h1>Regular expression</h1>
<p>A regular expression, commonly called a “regexp”, is a sequence of characters that define a search pattern.  It is mainly for use in pattern matching with strings, or string matching (i.e. it operates like a “find and replace” command). While it is a very powerful tool, it is also very dangerous because of its complexity.</p>
<img src="https://intranet.alxswe.com/images/contents/sysadmin/concepts/29/regex_now_2_problems.jpg" alt="Regex expression" width="100%" height="auto"/>
<h2>Background Context</h2>
<p>For this project, you have to build your regular expression using Oniguruma, a regular
expression library that which is used by Ruby by default. Note that other regular expression
libraries sometimes have different properties.</p>
<p>Because the focus of this exercise is to play with regular expressions (regex), here is
the Ruby code that you should use, just replace the regexp part, meaning the code in between the <code>//</code>:
<pre>
<code>
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</code>
</pre>

<h2>Resources</h2>
<details>
<summary>Regular Expression</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/mkcB0Yk1/image.png' border='0' alt='image'/></a>
<ul>
  <li>Links from screenshot
  <ul>
      <li><a href="https://www.regular-expressions.info/">regular-expressions</a></li>
      <li><a href="https://www.w3schools.com/jsref/jsref_obj_regexp.asp">Play with regexp</a></li>
      <li><a href="https://rubular.com/">Ruby</a></li>
      <li><a href="https://regex101.com/">PHP/Javascript/Python</a></li>
  </ul>
  </li>
</ul>
</details>

- [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
- [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
- [Rubular is your best friend](https://rubular.com/)
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

## Tasks

<details>
<summary><a href="./0-simply_match_school.rb">0. Simply matching School</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/1zCjqLRw/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./1-repetition_token_0.rb">1. Repetition Token #0</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/dtgN5CgX/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./2-repetition_token_1.rb">2. Repetition Token #1</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/QMLWH8wv/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./3-repetition_token_2.rb">3. Repetition Token #2</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/6pZfHmXJ/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./4-repetition_token_3.rb">4. Repetition Token #3</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/sf92mzKN/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./5-beginning_and_end.rb">5. Not quite HBTN yet</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/TwdsXrMm/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./6-phone_number.rb">6. Call me maybe</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/Kz1Hzmjv/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./7-OMG_WHY_ARE_YOU_SHOUTING.rb">7. OMG WHY ARE YOU SHOUTING?</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/yYsypVKg/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./100-textme.rb">8. Textme</a></summary><br>
<a href='https://postimg.cc/3kzNT3Sb' target='_blank'><img src='https://i.postimg.cc/wBjmDvhH/image.png' border='0' alt='image'/></a>
<ul>
  <li>Links from screenshot
  <ul>
      <li><a href="./text_messages.log">text messages log file</a></li>
  </ul>
  </li>
</ul>
