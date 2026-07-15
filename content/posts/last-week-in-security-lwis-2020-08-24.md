Title: Last Week in Security (LWiS) - 2020-08-24
Date: 2020-08-24 22:45
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-08-24
Author: Erik
Summary: Kerberoasting without SPNs by <a href="https://twitter.com/_mohemiv" target="_blank">@_mohemiv</a>, spoof any gmail/gsuite customer with a technique from <a href="https://twitter.com/ezhes_" target="_blank">@ezhes_</a>, SharpBlock in memory loading by <a href="https://twitter.com/_EthicalChaos_" target="_blank">@_EthicalChaos_</a>, new COM based lateral movement from <a href="https://twitter.com/el3ct71k" target="_blank">@El3ct71k</a>, Windows LPE by <a href="https://twitter.com/RedVuln" target="_blank">@RedVuln</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-08-17 to 2020-08-24.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://ezh.es/blog/2020/08/the-confused-mailman-sending-spf-and-dmarc-passing-mail-as-any-gmail-or-g-suite-customer/" target="_blank">The Confused Mailman: Sending SPF and DMARC passing mail as any Gmail or G Suite customer</a> Due to missing verification when configuring mail routes, both Gmail’s and any G Suite customer’s strict DMARC/SPF policy may be subverted by using G Suite’s mail routing rules to relay and grant authenticity to fraudulent messages. This would have been a phishing goldmine, but luckily was patched quickly following public release.</li>
<li><a href="https://www.elastic.co/blog/whats-new-elastic-security-7-9-0-free-endpoint-security" target="_blank">Elastic Security 7.9 adds anti-malware, prebuilt cloud protections, and more</a>.  While it is "free," any useful service (i.e. alerts) requires a paid license. Interested to see if the agent is supported by <a href="https://opendistro.github.io/for-elasticsearch/" target="_blank">Open Distro</a> soon. If you want to test it out in your lab try <a href="https://github.com/dirtyfilthy/siem-from-scratch" target="_blank">siem-from-scratch</a>.</li>
<li><a href="https://www.crowdstrike.com/blog/state-of-exploit-development-part-2/" target="_blank">The Current State of Exploit Development, Part 2</a>. Just like part 1, this post walks through some modern exploit mitigations that are making the attacker's life harder. Hungry for more? Check out <a href="https://connormcgarr.github.io/examining-xfg/" target="_blank">Exploit Development: Between a Rock and a (Xtended Flow) Guard Place: Examining XFG</a>.</li>
<li><a href="https://blog.apnic.net/2020/08/21/chromiums-impact-on-root-dns-traffic/" target="_blank">Chromium’s impact on root DNS traffic</a>. Interesting that nearly 50% of traffic seen by root DNS servers are from Chromium based browsers doing DNS interception checks. This is the consequence of adding 3 DNS requests per startup to an app that is used by 70% of users on the internet.</li>
<li><a href="https://kottke.org/20/08/researchers-can-duplicate-keys-from-the-sounds-they-make-in-locks" target="_blank">Researchers Can Duplicate Keys from the Sounds They Make in Locks</a>. Practical - no, Cool - yes. Another step toward the dystopian super surveillance future where high speed footage of the leaves near your front door can be used to recreate the sounds your key makes and therefore cut a copy of your key.</li>
<li><a href="https://www.kali.org/news/kali-2020-3-release/" target="_blank">Kali Linux 2020.3 Release</a>. The de-facto default penetration testing distro releases its latest update. High DPI support, new icons, bash-&gt;ZSH, and cleaner setup process are the highlights, as well as updated packages of course.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://swarm.ptsecurity.com/kerberoasting-without-spns/" target="_blank">Performing Kerberoasting without SPNs</a> adds the -usersfile option to GetUserSPNs.py, which requests tickets for each line from the specified file using the NT-ENTERPRISE type, and changed the default behavior from usage of service principal names to usage of SAM Account Names. This allows the retrieval of a Kerberos ticket in scenarios that otherwise would have failed, and allows mass-checking a list of SAM accounts for Kerberos tickets, not just those accounts that have SPNs!</li>
<li><a href="https://posts.specterops.io/attacking-azure-azure-ad-part-ii-5f336f36697d" target="_blank">Attacking Azure &amp; Azure AD, Part II</a> introduces <a href="https://github.com/hausec/PowerZure" target="_blank">PowerZure</a> 2.0 which add all kinds of neat features, my favorite being New-AzureIntuneScript which uploads a PowerShell script to Intune which will execute by default against all devices. Hope you have load balancing on your C2 server for all the shells that will call back!</li>
<li><a href="https://itm4n.github.io/dotnet-sdk-eop/" target="_blank">Windows .Net Core SDK Elevation of Privilege</a>. <a href="https://twitter.com/redvuln" target="_blank">@RedVuln</a> <a href="https://redvuln.com/net_privesc/" target="_blank">found</a> the original vulnerability, and <a href="https://twitter.com/itm4n" target="_blank">@itm4n</a> dug into it. A nice Windows privesc for a user that has the .NET Core SDK installed, and isn't a local admin anymore, or SYSTEM persistence if they are.</li>
<li><a href="https://unit42.paloaltonetworks.com/wireshark-tutorial-decrypting-https-traffic/" target="_blank">Wireshark Tutorial: Decrypting HTTPS Traffic</a> is a basic but well done tutorial.</li>
<li><a href="https://offensi.com/2020/08/18/how-to-contact-google-sre-dropping-a-shell-in-cloud-sql/" target="_blank">How to contact Google SRE: Dropping a shell in cloud SQL</a>. SQL injection in Cloud SQL! Just when you think the major cloud providers have security on lock, you read something like this. The good news is how fast the SRE responded and the issues were dealt with.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/tyranid/DumpReparsePoints" target="_blank">DumpReparsePoints</a> is a new tool from <a href="https://twitter.com/tiraniddo" target="_blank">@tiraniddo</a> that dumps all reparse points of an NTFS drive on Windows. What is a reparse point? Fun things like symbolic links, hard links, and directory junctions, among others. I'm sure this means there are about to be more file-link based attacks/LPEs from James soon.</li>
<li><a href="https://github.com/CCob/SharpBlock" target="_blank">SharpBlock</a>. The tool isn't new but the fact you can load binaries via http or over a named pipe and inject them into memory is a huge new feature. Take inspiration from this for your next EDR bypassing loader.</li>
<li><a href="https://github.com/slyd0g/LNKMod" target="_blank">LNKMod</a> is a C# project to create or modify existing LNKs.</li>
<li><a href="https://github.com/projectdiscovery/mapcidr" target="_blank">mapcidr</a> is a small utility program to perform multiple operations for a given subnet/CIDR ranges.</li>
<li><a href="https://github.com/aquasecurity/tracee" target="_blank">tracee</a> is a lightweight and easy to use container and system tracing tool. It allows you to observe system calls and other system events in real time. Intended as a debugging tool, tracee has implications for Linux red team tools for process monitoring system side.</li>
<li><a href="https://github.com/TimeToogo/tunshell" target="_blank">tunshell</a> is billed as a "remote shell into ephemeral environments" and acts a bit like <a href="https://ngrok.com/" target="_blank">ngrok</a> + a shell. The beauty of tunshell is that its client is a statically-linked, pre-compiled binary which can be installed by downloading it with a one-liner script. It was built for debugging CI environments, but there are obvious red team use cases.</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2047" target="_blank">CmpDoReDoCreateKey Arbitrary Registry Key Creation EoP</a> and <a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2048" target="_blank">CmpDoReadTxRBigLogRecord Memory Corruption EoP</a> were patched and dropped with PoCs that aren't ready for use on an engagement but would be good starting points for weaponization.</li>
<li><a href="https://www.activecyber.us/activelabs/windows-appx-deployment-service-local-privilege-escalation-cve-2020-1488" target="_blank">Windows AppX Deployment Service Local Privilege Escalation (CVE-2020-1488)</a>. Another AppX bug leads to local privilege escalation that reminds me of <a href="https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1064" target="_blank">CVE-2019-1064</a>.</li>
<li><a href="https://github.com/ScorpionesLabs/DVS" target="_blank">DVS</a> - D(COM) V(ulnerability) S(canner) AKA Devious swiss army knife - Lateral movement using DCOM Objects. The DVS framework contains various ways to bypass remote hardening against DCOM by re-enabling DCOM access remotely and automatically grant the required permissions to the attacking user. The framework can also revert changes on the remote machine to their original state, prior to the attack.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/b4rtik/SharpKatz" target="_blank">SharpKatz</a> is a C# port if of mimikatz sekurlsa::logonpasswords, sekurlsa::ekeys and lsadump::dcsync commands for your C# in memory needs.</li>
<li><a href="https://www.wizer-training.com/" target="_blank">Wizer Training</a> is a freemium phishing training platform. Very interesting model, and I'm excited to try it out. Don't be fooled by wizertraining.com which was briefly redirecting to knowbe4.com. If the competition is playing dirty, you must be doing something right!</li>
<li><a href="https://github.com/rverton/wonitor" target="_blank">wonitor</a> is a fast, zero config web endpoint change monitor. For comparing responses, a selected list of http headers and the full response body is stored on a local key/value store file. No configuration needed.</li>
<li><a href="https://github.com/chenjj/espoofer" target="_blank">espoofer</a> is an email spoofing testing tool that aims to bypass SPF/DKIM/DMARC and forge DKIM signatures.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
