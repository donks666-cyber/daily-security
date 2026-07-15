Title: Last Week in Security (LWiS) - 2020-04-06
Date: 2020-04-06 10:20
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-04-06
Author: Erik
Summary: A pile of Zoom issues, expanded ATT&amp;CK matrix, DeskPro RCE, a journey into Safari for unauthorized camera access, the weekly Windows LPE, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-03-30 to 2020-04-06.
MITRE ATT&amp;CK techniques are in brackets where appropriate.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><dl>
<dt>Zoom issues. With great marketshare comes great responsibility to not be a dumpster fire of security. Lest we forget last year when their macOS app <a href="https://medium.com/bugbountywriteup/zoom-zero-day-4-million-webcams-maybe-an-rce-just-get-them-to-visit-your-website-ac75c83f4ef5" target="_blank">installed a web server that listened on localhost</a> and allowed for remote code execution and did not uninstall with the app. Thankfully that has been corrected and the issues discovered recently are less severe.</dt>
<dd><ul>
<li><a href="https://objective-see.com/blog/blog_0x56.html" target="_blank">The 'S' in Zoom, Stands for Security</a>. The macOS whisperer <a href="https://twitter.com/patrickwardle" target="_blank">Patrick Wardle</a> goes over past issues and digs into the current installer's "tricks" that are also seen in a lot of macOS malware. Pro tip: after clicking "Launch meeting" twice for a Zoom meeting in Chrome it will give the option to "Continue in browser." No client software required.</li>
<li><a href="https://www.reuters.com/article/us-spacex-zoom-video-commn/elon-musks-spacex-bans-zoom-over-privacy-concerns-memo-idUSKBN21J71H" target="_blank">Elon Musk's SpaceX bans Zoom over privacy concerns</a>. Not an unexpected move given all the news here. The most troubling quote is from a Zoom blog post: "Zoom has always strived to use encryption to protect content in as many scenarios as possible, and in that spirit, we used the term end-to-end encryption." End-to-end encryption is a technical term, not something you can have "in spirit."</li>
<li><a href="https://krebsonsecurity.com/2020/04/war-dialing-tool-exposes-zooms-password-problems/" target="_blank">‘War Dialing’ Tool Exposes Zoom’s Password Problems</a>. A new tool called zWarDial is able to find a surprising number of Zoom meetings without passwords by brute forcing meeting IDs. Regardless of your conferencing solution, use a strong password!</li>
<li><a href="https://theintercept.com/2020/04/03/zooms-encryption-is-not-suited-for-secrets-and-has-surprising-links-to-china-researchers-discover/" target="_blank">Zoom’s Encryption Is “Not Suited for Secrets” and Has Surprising Links to China, Researchers Discover</a>. 5 out of 73 Key managment servers are in China and are used for some calls that have no nexus in China and makes questionable encryption choices (128 AES in ECB mode?!).</li>
<li>There has been some press over Zoom "allowing" UNC paths to "leak windows password hashes" which in my opinion is a stretch at best. Zoom is opening the links correctly, and it is Windows that is sending hashes. To me, this is not a Zoom issue.</li>
<li>Zoom seems to be taking this all quite well, and have <a href="https://twitter.com/patrickwardle/status/1245613529660411905" target="_blank">made concrete steps and promises to improve</a>.</li>
<li><a href="https://jitsi.org/jitsi-meet/" target="_blank">Jitsi Meet</a> a more secure and self-hostable option for video conferencing (a good install and comparison to Big Blue Button <a href="https://jianmin.dev/2020/mar/29/host-your-own-web-conferences/" target="_blank">here</a>). Signal also is a great choice for everyday use and 1 on 1 video calls.</li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://medium.com/mitre-attack/attack-subs-what-you-need-to-know-99bce414ae0b" target="_blank">ATT&amp;CK with Sub-Techniques — What You Need to Know</a>. MITRE releases a new version of the ATT&amp;CK matrix with sub-techniques! Check out the new matrix <a class="m-text m-dim" href="https://attack.mitre.org/beta/" target="_blank">here</a>.</li>
<li><a href="https://www.documentcloud.org/documents/6824735-Declaration-of-Shalev-Hulio-in-Support-of.html" target="_blank">Facebook tried to buy NSO iOS tool Pegasus</a> (see point 10). NSO goes nuclear in their latest court filing by claiming that Facebook tried to pay them to hack iOS users for data collection. Extraordinary claims require extraordinary evidence, as NSO is certainly in a position to gain from bad press about Facebook given the pending Whatsapp lawsuit.</li>
<li><a href="https://blog.cloudflare.com/introducing-1-1-1-1-for-families/" target="_blank">Introducing 1.1.1.1 for Families</a>. Cloudflare, one of the few (only?) <a href="https://blog.cloudflare.com/announcing-the-results-of-the-1-1-1-1-public-dns-resolver-privacy-examination/" target="_blank">audited</a> DNS resolvers introduced two new options, 1.1.1.2 will not resolve known malware domains, and 1.1.1.3 will not resolve known malware domains or "adult content." DNS filters are by no means a full filtering solution, but if all it takes to block some malware is a DNS entry change and the provider has a track record of privacy, it may be a good option for average users.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.redforce.io/attacking-helpdesks-part-1-rce-chain-on-deskpro-with-bitdefender-as-case-study/" target="_blank">Attacking HelpDesks Part 1: RCE Chain on DeskPro, with Bitdefender as a Case Study</a> is a wild ride that chains a few bugs to get RCE on BitDefender's infrastructure. Well done redforce and I look forward to the next few posts on other help desk software. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</li>
<li><a href="https://en.hackndo.com/ntlm-relay/" target="_blank">NTLM Relay</a> might be the most comprehensive resource for NTLM relay attack details I have come across. This will be come a reference for future NTLM questions. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1171/" target="_blank">T1171 LLMNR/NBT-NS Poisoning and Relay</a>]</li>
<li><a href="https://www.ryanpickren.com/webcam-hacking" target="_blank">Webcam Hacking - The story of how I gained unauthorized Camera access on iOS and macOS</a>. Buckle up for a bumpy ride into iOS and macOS internals and the eventual creative bug chain that allows camera access to a malicious website. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1125/" target="_blank">T1125 Video Capture</a>]</li>
<li><a href="https://techanarchy.net/blog/cve-2020-10560-ossn-arbitrary-file-read" target="_blank">CVE-2020-10560 - OSSN Arbitrary File Read</a>. An authentication bypass via custom crypto, to eventually get arbitrary file read. Interesting web app pen-testing process presented here. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1190/" target="_blank">T1190 Exploit Public-Facing Application</a>]</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://fortynorthsecurity.com/blog/eyewitness-looking-sharp/" target="_blank">EyeWitness - Looking Sharp</a> introduces the C# version of the EyeWitness website screenshot tool for use with Cobalt Strike or other C# implants. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1046/" target="_blank">T1046 Network Service Scanning</a>]</li>
<li><a href="https://github.com/projectdiscovery/nuclei" target="_blank">nuclei</a> - Project Discovery keeps the hits coming with nuclei, a fast tool for configurable targeted scanning based on templates offering massive extensibility and ease of use. Think of it as an open source Nessus. Be sure to grab the <a href="https://github.com/projectdiscovery/nuclei-templates" target="_blank">templates</a> too. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1046/" target="_blank">T1046 Network Service Scanning</a>]</li>
<li><a href="https://github.com/orf/dirscan" target="_blank">dirscan</a> is a high performance tool for summarizing large directories or drives. Written in rust, this cross platform tool is blazing fast and works on local and network drives. If you need to quickly get a handle on where things are on a machine, this could be your new best friend. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1005/" target="_blank">T1005 Data from Local System</a>]</li>
<li><a href="https://github.com/sailay1996/magnifier0day" target="_blank">magnifier0day</a> is this week's Windows local privilege escalation exploit. This one requires a writable path in %PATH% but after that it is as easy as two hotkeys to a SYSTEM shell. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1068/" target="_blank">T1068 Exploitation for Privilege Escalation</a>]</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/ambionics/phpggc" target="_blank">phpggc</a> is a library of PHP unserialize() payloads along with a tool to generate them, from command line or programmatically.</li>
<li><a href="https://github.com/FooBallZ/pulsar" target="_blank">pulsar</a> is an automated network footprint scanner for Red Teams, Pentesters and Bounty Hunters. It's focused on discovery of an organization's public facing assets with minimal knowledge about its infrastructure. [<a class="m-text m-dim" href="https://attack.mitre.org/techniques/T1046/" target="_blank">T1046 Network Service Scanning</a>]</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
