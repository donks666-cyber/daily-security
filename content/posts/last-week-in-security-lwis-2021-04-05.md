Title: Last Week in Security (LWiS) - 2021-04-05
Date: 2021-04-05 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-04-05
Author: Erik
Summary: PATH shim (<a href="https://twitter.com/djhohnstein" target="_blank">@djhohnstein</a>), C2 profile randomizer (<a href="https://twitter.com/joevest" target="_blank">@joevest</a>), website to wordlist tool (<a href="https://twitter.com/Matt_Grandy_" target="_blank">@Matt_Grandy_</a>), DLL side-loading fixes (<a href="https://twitter.com/1ndahous3" target="_blank">@1ndahous3</a>), a new 🥔 tool (<a href="https://twitter.com/micahvandeusen" target="_blank">@micahvandeusen</a>), txt files that leak (<a href="https://twitter.com/PaulosYibelo" target="_blank">@PaulosYibelo</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-03-29 to 2021-04-05.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://therecord.media/phone-numbers-for-533-million-facebook-users-leaked-on-hacking-forum/" target="_blank">Phone numbers for 533 million Facebook users leaked on hacking forum</a>. The data is from a 2019 scrape that abused the contact import feature, and has been circulating in private since then. Now however, anyone who knows your name can look up the phone number used to register your facebook account.</li>
<li><a href="https://krebsonsecurity.com/2021/03/whistleblower-ubiquiti-breach-catastrophic/" target="_blank">Whistleblower: Ubiquiti Breach “Catastrophic”</a>. Despite the initially downplayed public statement in January, an insider claims the attacker "gained root administrator access to all Ubiquiti AWS accounts, including all S3 data buckets, all application logs, all databases, all user database credentials, and secrets required to forge single sign-on (SSO) cookies." Ubiquiti has since issued a <a href="https://krebsonsecurity.com/2021/04/ubiquiti-all-but-confirms-breach-response-iniquity/" target="_blank">new statement</a> that did not dispute any of the facts and hinted the perpetrator may have been an insider, or "an individual with intricate knowledge of our cloud infrastructure."</li>
<li><a href="https://outflank.nl/blog/2021/04/02/our-reasoning-for-outflank-security-tooling/" target="_blank">Our reasoning for Outflank Security Tooling</a>. Outflank, a well known top-tier adversary simulation firm out of the Netherlands, is offering its in-house offensive toolset for a yearly license of €40,000. I agree with their thesis that effective red teams now have to be excellent developers/R&amp;D practitioners and that was not the case 5 or more years ago. Hopefully this business model is sustainable - I think it will be. More details on the <a href="https://outflank.nl/services/outflank-security-tooling/" target="_blank">product page</a>.</li>
<li><a href="https://blog.google/threat-analysis-group/update-campaign-targeting-security-researchers/" target="_blank">Update on campaign targeting security researchers</a>. The North Korean actors that targeted security researchers with malicious project files in January 2021 have stood up a new potential watering hole. In this case, Google's Threat Analysis Group was able to notice before the site could host any malicious content.</li>
<li><a href="https://en.wikipedia.org/wiki/Google_LLC_v._Oracle_America,_Inc.#Supreme_Court" target="_blank">Google LLC v. Oracle America, Inc.</a>. "The Court ruled that Google's use of the Java APIs was within the bounds of fair use, reversing the Federal Circuit Appeals Court ruling and remanding the case for further hearing." While it isn't a total victory (it didn't rule that APIs couldn't be copyrighted), it's still a win.</li>
<li><a href="https://developer.greynoise.io/reference/community-api" target="_blank">Community API</a>. Greynoise has been a useful tool for SOCs to determine if the traffic they are seeing is legitimate attacks or just noise like known scanners. Now there is a free to use community API!</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.cloudflare.com/how-to-execute-an-object-file-part-2/" target="_blank">How to execute an object file: Part 2</a>. This post picks up where the <a href="https://blog.cloudflare.com/how-to-execute-an-object-file-part-1/" target="_blank">last one</a> left off and expands the loader to handle static constant data and global variables.</li>
<li><a href="https://posts.specterops.io/man-in-the-terminal-65476e6165b9" target="_blank">Man in the Terminal</a>. On Linux or macOS targets, PATH variable manipulation can allow your program to be executed before the actual program the user invokes, allowing you to shim it and retrieve credentials and other sensitive information. A proof of concept shim called <a href="https://github.com/djhohnstein/cliProxy" target="_blank">cliProxy</a> is available. A simple improvement would be for cliProxy to automatically detect the program it is invoked as and search the real PATH for that binary to proxy. That way you could compile once, and deploy for many target binaries.</li>
<li><a href="https://zeroperil.co.uk/hookdump/" target="_blank">HookDump</a>. By using LoadLibrary and reading the DLL from disk, HookDump can compare the exported functions to detect hooks with low (or no?) false positives. Grab the <a href="https://github.com/zeroperil/HookDump" target="_blank">code</a> on GitHub.</li>
<li><a href="https://medium.com/@1ndahous3/safe-code-pitfalls-dll-side-loading-winapi-and-c-73baaf48bdf5" target="_blank">Safe code &amp; pitfalls: DLL side-loading, WinAPI and C++</a>. DLL side-loading is a common persistence technique, but it can be difficult to write the "remediation" section of a report that finds usable DLL side-loading on an app assessment. This is the best blog I have found that provides technical details on how to prevent side-loading in C++.</li>
<li><a href="https://www.secarma.com/three-ways-of-using-msbuild-to-beat-crowdstrike/" target="_blank">Three ways of using MSBuild to beat CrowdStrike</a>. MSBuild has been a favorite <a href="https://lolbas-project.github.io/" target="_blank">LOLBin</a> for years now, and it still is undetected in many cases!</li>
<li><a href="https://micahvandeusen.com/the-power-of-seimpersonation/" target="_blank">The Power of SeImpersonation</a>. Just when you thought there couldn't possibly <a href="https://github.com/CCob/SweetPotato" target="_blank">be</a> <a href="https://github.com/johnjohnsp1/reflectivepotato" target="_blank">any</a> <a href="https://github.com/TsukiCTF/Lovely-Potato" target="_blank">more</a> <a href="https://github.com/decoder-it/lonelypotato" target="_blank">potato</a> <a href="https://github.com/ohpe/juicy-potato" target="_blank">exploit</a> <a href="https://github.com/antonioCoco/RoguePotato" target="_blank">variants</a> another one drops. This new variant focuses on the ability to respond to HTTP requests or named pipe write. The code is available as <a href="https://github.com/micahvandeusen/GenericPotato" target="_blank">GenericPotato</a>.</li>
<li><a href="https://www.paulosyibelo.com/2021/04/this-man-thought-opening-txt-file-is.html" target="_blank">This man thought opening a TXT file is fine, he thought wrong. macOS CVE-2019-8761</a>. Textedit is the notepad.exe of macOS and it will render HTML for you without asking. Using some iframedoc and style magic, even without javascript Paulos is able to exfil data. Impressive work! I always run <cite>defaults write com.apple.TextEdit RichText -bool false</cite> on a new mac to prevent the rich text rendering anyway, now it's a security hardening feature.</li>
<li><a href="https://rev.ng/blog/pagebuster/post.html" target="_blank">PageBuster: stealthily dump all the code ever executed</a>. This tool can dump all executable pages from memory which is great for things like analyzing packed malware in a sandbox vs reverse engineering the packer and unpacking it by hand.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/nccgroup/PMapper" target="_blank">PMapper</a> is a script and library for identifying risks in the configuration of AWS Identity and Access Management (IAM) for an AWS account or an AWS organization. It models the different IAM Users and Roles in an account as a directed graph, which enables checks for privilege escalation and for alternate paths an attacker could take to gain access to a resource or action in AWS.</li>
<li><a href="https://github.com/threatexpress/random_c2_profile" target="_blank">random_c2_profile</a> is a project designed to generate malleable c2 profiles based on the reference profiles <a href="https://github.com/threatexpress/malleable-c2/" target="_blank">here</a>. This makes totally random profiles, so you may want to manually make it <em>less</em> random.</li>
<li><a href="https://github.com/mattgrandy/WordlistSmith" target="_blank">WordlistSmith</a> is a tool to quickly scrape a website and generate a wordlist and is multithreading capable.</li>
<li><a href="https://github.com/klezVirus/CheeseTools/tree/master/CheeseRDP" target="_blank">CheeseRDP</a> is a single C# binary that can be run via .NET Reflection and will inject into mstsc.exe to steal RDP credentials. No need to drop a DLL to disk!</li>
<li><a href="https://github.com/Flangvik/SharpProxyLogon" target="_blank">SharpProxyLogon</a> is a fully featured exploit for ProxyLogon (the Exchange RCE chain) that can either drop a webshell or inject shellcode into svchost.exe as SYSTEM.</li>
<li><a href="https://github.com/rvrsh3ll/X-Commander" target="_blank">X-Commander</a> is an easy-to-use python tool for attacking MySQLX or XDevAPI, brute forcing and querying.</li>
<li><a href="https://github.com/tonarino/innernet" target="_blank">innernet</a> is a private network system that uses WireGuard under the hood. While WireGuard is awesome, it's just a really good VPN and nothing more. Innernet looks to solve some of the comfort issues with WireGuard. The <a href="https://blog.tonari.no/introducing-innernet" target="_blank">announcement blog post</a> has the details.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/eciavatta/caronte" target="_blank">caronte</a> is a tool to analyze the network flow during capture the flag events of type attack/defense. It reassembles TCP packets captured in pcap files to rebuild TCP connections, and analyzes each connection to find user-defined patterns.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
