# Blackbox
Category: Web

## Description
Author: `Mr. Blade`

I took a survey to find our dev's least favorite type of web challenge. The results of my survey showed that blackbox web is by far the most frustrating type of web challenge. Let's see what your opinion of it is.

NOTE: flag format for this challenge is `tamuctf{...}`

[http://blackbox.tamuctf.com](http://blackbox.tamuctf.com)

## Write-up
- We observed that the web pages are accessed using the page GET parameter, which suggests the possibility of a file inclusion vulnerability.
- We discovered the existence of `/robots.txt`, which leaked the presence of a `.git` repository, potentially containing the source code of the web application.
- This indicates that we can use tools like `git-dumper` to extract the repository.
- During the repository extraction, we identified an `admin.php` file that attempts to reveal the file `/flag.txt` under certain conditions.
- We can exploit a local file inclusion vulnerability using PHP filter chains, enabling us to achieve remote code execution without uploading a file.
- The `php_filter_chain_generator.py` script, available at [https://github.com/synacktiv/php_filter_chain_generator/blob/main/php_filter_chain_generator.py](https://github.com/synacktiv/php_filter_chain_generator/blob/main/php_filter_chain_generator.py), can be utilized to generate PHP filter chains.
- The command to generate the filter chain payload that retrieves the flag is `python3 php_filter_chain_generator.py --chain '<?echo system("cat /flag.txt"); ?> `
- By accessing `/?page=<payload>`, the contents of the `/flag.txt` file will be exposed.

Flag: `tamuctf{my_f4v0rit4_7yp3_0f_w3b_ch4113ng3}`
