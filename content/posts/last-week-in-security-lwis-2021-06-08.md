Title: Last Week in Security (LWiS) - 2021-06-08
Date: 2021-06-08 23:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-06-08
Author: Erik
Summary: Bypassing NAC (<a href="https://twitter.com/theluemmel" target="_blank">@theluemmel</a>), Outlook COM tool (<a href="https://twitter.com/eks_perience" target="_blank">@eks_perience</a>), Transacted Hollowing (<a href="https://twitter.com/hasherezade" target="_blank">@hasherezade</a>), SeTrustedCredmanAccess research and tooling (<a href="https://twitter.com/tiraniddo" target="_blank">@tiraniddo</a>, <a href="https://twitter.com/Pullerze" target="_blank">@Pullerze</a>), netcat with raw sockets (<a href="https://twitter.com/Itsuugo" target="_blank">@Itsuugo</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-05-31 to 2021-06-08 (bonus day!).</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf" target="_blank">VAN BUREN v. UNITED STATES</a>. The CFAA cannot be used to prosecute rogue employees who have legitimate access to work-related resources (in this case police officer running unsanctioned database searches for money), which will need to be prosecuted under different charges. This adds weight to the 9th circuit court ruling that <a href="https://cdn.ca9.uscourts.gov/datastore/opinions/2019/09/09/17-16783.pdf" target="_blank">ToS violations are not a crime</a>.</li>
<li><a href="https://krebsonsecurity.com/2021/06/justice-dept-claws-back-2-3m-paid-by-colonial-pipeline-to-ransomware-gang/" target="_blank">Justice Dept. Claws Back $2.3M Paid by Colonial Pipeline to Ransomware Gang</a>. The DOJ stated that the ransom payment "had been transferred to a specific address, for which the FBI has the 'private key,' or the rough equivalent of a password needed to access assets accessible from the specific Bitcoin address" which caused some to believe the FBI had either "cracked" Bitcoin (no) or seized a custodial wallet. I doubt the DarkSide crew is foolish enough to use a US based custodial exchange, and therefore the logical answer is _someone_ shelled DarkSide and transferred the Bitcoin to an address the FBI happened to control.</li>
<li><a href="https://github.blog/2021-06-04-updates-to-our-policies-regarding-exploits-malware-and-vulnerability-research/" target="_blank">Updates to our policies regarding exploits, malware, and vulnerability research</a>. GitHub resolves their policy update on exploits in a reasonable manner. "Dual-use" security research is allowed, but you can't use GitHub itself as part of an attack (i.e. use gists for C2) and as always it reserves the right to remove PoCs used in attacks.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.ret2.io/2021/06/02/pwn2own-2021-jsc-exploit/" target="_blank">32 bits, 32 gigs, 1 click... Exploitation of a JavaScriptCore WebAssembly Vulnerability</a>. This post examines a vulnerability in the WebAssembly subsystem of JavaScriptCore, the JavaScript engine used in WebKit and Apple Safari. The issue was patched in Safari 14.1.1. This vulnerability was discovered through source review and weaponized to achieve remote code execution. The post stops short of RCE via a kernel driver exploit, but the source code is <a href="https://github.com/ret2/Pwn2Own-2021-Safari" target="_blank">available</a></li>
<li><a href="https://blog.christophetd.fr/retrieving-aws-security-credentials-from-the-aws-console/" target="_blank">Retrieving AWS security credentials from the AWS console</a>. If you can dump browser cookies you can now extract an AWS token to use in the CLI thanks to the new CloudShell and an undocumented API.</li>
<li><a href="https://luemmelsec.github.io/I-got-99-problems-but-my-NAC-aint-one/" target="_blank">I got 99 problems but my NAC ain´t one</a>. Think your fancy 802.1x is going to stop a determined adversary? Think again. The start of the show is <a href="https://github.com/scipag/nac_bypass" target="_blank">nac_bypass</a>.</li>
<li><a href="https://www.optiv.com/insights/source-zero/blog/kerberos-domains-achilles-heel" target="_blank">Kerberos - A Domains Achille's Heel</a>. Gives a good overview of Kerberos, Silver and Golden Tickets.</li>
<li><a href="https://passthehashbrowns.github.io/dynamic-payload-generation-with-mingw" target="_blank">Dynamic payload generation with mingw</a>. This in-depth post explores cross-compilation of Windows binaries and shellcode on Linux using mingw64 and contains some nifty tricks - like how to pull shellcode from the .text section of an exe.</li>
<li><a href="https://infinitelogins.com/2021/06/06/your-microsoft-teams-chats-arent-as-private-as-you-think/" target="_blank">Your Microsoft Teams chats aren’t as private as you think..</a>. This post includes a handy command pipeline to parse messages from a log file Teams stores on disk (unencrypted). There could be some good information in those chats (passwords, etc).</li>
<li><a href="https://frichetten.com/blog/xss_in_aws_console/" target="_blank">XSS in the AWS Console</a>. This post explores two instances of XSS in the AWS console. They are now fixed. It has everything you can ask for: 0days in AWS, a CSP bypass, and memes.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/aojea/netkat" target="_blank">netkat</a> is a netcat version using raw sockets to avoid iptables and/or other OS filtering mechanisms. This could come in handy if you land inside a container running with sufficient privileges to do network shenanigans.</li>
<li><a href="https://github.com/eksperience/KnockOutlook" target="_blank">KnockOutlook</a> is a C# project that interacts with Outlook's COM object in order to perform a number of operations useful in red team engagements. Be sure to check out <a href="https://github.com/checkymander/Carbuncle" target="_blank">Carbuncle</a> and <a href="https://github.com/ThunderGunExpress/OutlookToolbox_v2" target="_blank">OutlookToolbox_v2</a> for more complete feature sets.</li>
<li><a href="https://github.com/secureworks/PhishInSuits" target="_blank">PhishInSuits</a> is a tool to automate OAuth device code phishing using verified apps with twilio powered phishing SMS messages.</li>
<li><a href="https://github.com/antman1p/Conf-thief" target="_blank">Conf-thief</a> will connect to Confluence's API using an access token, export to PDF, and download the Confluence documents that the target has access to. It allows you to use a dictionary/keyword search file to search all files in the target Confluence for potentially sensitive data. Check out the blog post: <a href="https://antman1p-30185.medium.com/stealing-all-of-the-confluence-things-94bd96a84dc0" target="_blank">Stealing All of the Confluence Things</a>.</li>
<li><a href="https://github.com/brightio/penelope" target="_blank">penelope</a> is an advanced shell handler. Its main aim is to replace netcat as shell catcher during exploiting RCE vulnerabilities. It works on Linux and macOS and the only requirement is Python 3.</li>
<li><a href="https://github.com/hasherezade/transacted_hollowing" target="_blank">transacted_hollowing</a> is a PE injection technique, hybrid between Process Hollowing and Process Doppelgänging - as seen in the Osiris dropper. Check out the <a href="https://blog.malwarebytes.com/threat-analysis/2018/08/process-doppelganging-meets-process-hollowing_osiris/" target="_blank">blog post</a> for all the details.</li>
<li><a href="https://github.com/blackarrowsec/Malleable-C2-Profiles/blob/master/normal/microsoftteams_getonly.profile" target="_blank">microsoftteams_getonly.profile</a> is a C2 profile for Cobalt Strike that mimics the network traffic of Microsoft Teams. Be warned, Azure is now <a href="https://twitter.com/424f424f/status/1402266781532803073" target="_blank">shutting down accounts that use domain fronting</a>.</li>
<li><a href="https://github.com/GKNSB/payloadSecretary" target="_blank">payloadSecretary</a> can be used to automatically type long base64 encoded payloads into restricted environments (VDI, Citrix, etc).</li>
<li><a href="https://github.com/jsecu/CredManBOF" target="_blank">CredManBOF</a> is a BOF file to use with Cobalt Strike, dumping the credential manager by abusing the SeTrustedCredmanAccess Privilege. Original research was done by James Foreshaw and further information is located <a href="https://www.tiraniddo.dev/2021/05/dumping-stored-credentials-with.html" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/3lp4tr0n/BeaconHunter" target="_blank">BeaconHunter</a> is a behavior based monitoring and hunting tool built in C# tool leveraging ETW tracing. Blue teamers can use this tool to detect and respond to potential Cobalt Strike beacons. Red teamers can use this tool to research ETW bypasses and discover new processes that behave like beacons.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
