Title: Last Week in Security (LWiS) - 2022-04-04
Date: 2022-04-04 23:08
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-04-04
Author: Erik
Summary: Shared section abuse (<a href="https://twitter.com/BillDemirkapi" target="_blank">@BillDemirkapi</a>), ISOs and office MOTW (<a href="https://twitter.com/DidierStevens" target="_blank">@DidierStevens</a>), better fuzzing harnesses (<a href="https://twitter.com/h0mbre_" target="_blank">@h0mbre_</a>), PoshC2 Linux ELF loader (<a href="https://twitter.com/jdsnape" target="_blank">@jdsnape</a>), "Event pipes" for IPC (<a href="https://twitter.com/x86matthew" target="_blank">@x86matthew</a>), Linux LPE (<a href="https://twitter.com/pqlqpql" target="_blank">@pqlqpql</a>), .soap webshells (<a href="https://twitter.com/0xbad53c" target="_blank">@0xbad53c</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2022-03-28 to 2022-04-04.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.praetorian.com/blog/spring-core-jdk9-rce/" target="_blank">Spring Core on JDK9+ is vulnerable to remote code execution</a>. "Spring4Shell" aka "SpringShell" aka CVE-2022-22865 is a one-request RCE against some Spring Core installs (tomcat hosted). <a href="https://www.trustedsec.com/blog/cve-2022-22965-spring4shell-vulnerability/" target="_blank">TrustedSec</a> has technical goodies.</li>
<li><a href="https://azure.microsoft.com/en-us/blog/now-in-preview-azure-virtual-machines-with-ampere-altra-armbased-processors/" target="_blank">Now in preview: Azure Virtual Machines with Ampere Altra Arm-based processors</a>. You can spin up ARM VMs in Azure (Linux and Windows 11). The age of ARM is upon us. The feature is in preview, so you'll have to <a href="https://aka.ms/Arm64VMsPreview" target="_blank">fill out this form</a>.</li>
<li><a href="https://www.cobaltstrike.com/blog/building-upon-a-strong-foundation/" target="_blank">The price of Cobalt Strike for new customers will be $5,900 per user for a one-year license</a>. Bigger development team = bigger budget.</li>
<li><a href="https://about.gitlab.com/releases/2022/03/31/critical-security-release-gitlab-14-9-2-released/" target="_blank">GitLab Critical Security Release: 14.9.2, 14.8.5, and 14.7.7</a>. GitLab security releases often include serious vulnerability patches, but this one is especially bad. "A hardcoded password was set for accounts registered using an OmniAuth provider (e.g. OAuth, LDAP, SAML) in GitLab CE/EE versions 14.7 prior to 14.7.7, 14.8 prior to 14.8.5, and 14.9 prior to 14.9.2 allowing attackers to potentially take over accounts." You can see the change to o_auth/user.rb <a href="https://gitlab.com/gitlab-org/gitlab/-/merge_requests/76318/diffs#f4d654b98cc11d931e3f77ee61318adc95a52f12_235_233" target="_blank">here</a>.</li>
<li><a href="https://blog.didierstevens.com/2022/04/04/iso-files-with-office-maldocs-protected-view-in-office-2019-and-2021/" target="_blank">.ISO Files With Office Maldocs &amp; Protected View in Office 2019 and 2021</a>. After the news that <a href="https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805" target="_blank">macros will be blocked</a> by default this month, many attackers were comforted by the fact there are many ways to deliver a payload without a Mark-of-the-web. The Microsoft Office team has taken one option off the table with some specific ISO inspections. This is an Office feature, as Windows does not add the MOTW to files in an ISO. You can still use other formats in tools such as <a href="https://github.com/mgeeky/PackMyPayload" target="_blank">PackMyPayload</a>.</li>
<li><a href="https://www.bloomberg.com/news/articles/2022-03-30/apple-meta-gave-user-data-to-hackers-who-forged-legal-requests" target="_blank">Apple and Meta Gave User Data to Hackers Who Used Forged Legal Requests</a>. Why hack when you can just ask for data? <a href="https://krebsonsecurity.com/2022/03/fake-emergency-search-warrants-draw-scrutiny-from-capitol-hill/" target="_blank">KrebsOnSecurity</a> has more detail.</li>
<li><a href="https://twitter.com/Trezor/status/1510558771944333312?t=j7fyUCkbgpYDvV0cNwzmng&amp;s=09" target="_blank">MailChimp have confirmed that their service has been compromised by an insider targeting crypto companies.</a>. Time to update your threat models.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://googleprojectzero.blogspot.com/2022/03/forcedentry-sandbox-escape.html" target="_blank">FORCEDENTRY: Sandbox Escape</a>. This post focuses on the sandbox escape used in the wild GIF JBIG2 decoder-as-stack-based-VM exploit.</li>
<li><a href="https://www.atredis.com/blog/2022/03/29/veni-midi-vici-conquering-cve-2022-22657-and-cve-2022-22664" target="_blank">Veni, MIDI, Vici — Conquering CVE-2022-22657 and CVE-2022-22664</a>. The bugs aren't the coolest, but the technique of "associative fuzzing" is valid and underused.</li>
<li><a href="https://billdemirkapi.me/sharing-is-caring-abusing-shared-sections-for-code-injection/" target="_blank">Sharing is Caring: Abusing Shared Sections for Code Injection</a>. After being forced to <a href="https://twitter.com/BillDemirkapi/status/1508820739968880640" target="_blank">look for a new position</a> due to sharing of LASPUS$ victim IR report screenshots (I guess?), Bill is back to writing interesting technical blogs (although he never stopped). A loss for Zoom, a win for us!</li>
<li><a href="https://blog.sonarsource.com/php-supply-chain-attack-on-pear" target="_blank">PHP Supply Chain Attack on PEAR</a>. Insufficient randomness strikes again!</li>
<li><a href="https://h0mbre.github.io/Fuzzing-Like-A-Caveman-6/#" target="_blank">Fuzzing Like A Caveman 6: Binary Only Snapshot Fuzzing Harness</a>. Fuzzing is all about speed, so being able to reset state and feed input from memory means more test cases, and hopefully more unique crashes.</li>
<li><a href="https://www.fortinet.com/blog/threat-research/deep-panda-log4shell-fire-chili-rootkits" target="_blank">New Milestones for Deep Panda: Log4Shell and Digitally Signed Fire Chili Rootkits</a>. Digitally signed rootkit drivers are scary, but there are lots of potential IOCs here that should be detected. Even the digital signature should have been suspect in an enterprise (unless you are a game dev perhaps).</li>
<li><a href="https://www.x86matthew.com/view_post?id=eventpipe" target="_blank">EventPipe - An IPC method to transfer binary data between processes using event objects</a>. A clever, but perhaps low bandwidth way to do inter-process communication on Windows that may not be as detected as standard named pipes or shared memory.</li>
<li><a href="https://medium.com/@frycos/pwning-3cx-phone-management-backends-from-the-internet-d0096339dd88" target="_blank">Pwning 3CX Phone Management Backends from the Internet</a>. This is an interesting journey from "whats on shoadan" to RCE.</li>
<li><a href="https://red.0xbad53c.com/red-team-operations/initial-access/webshells/iis-soap" target="_blank">IIS - SOAP</a>. IIS will process .soap files, enabling webshells with this little known extension.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://labs.nettitude.com/blog/introducing-poshc2-v8-0/" target="_blank">Introducing PoshC2 v8.0</a>. BOF compatibility, and a very slick Linux loader make version 8 worth checking out.</li>
<li><a href="https://github.com/pqlx/CVE-2022-1015" target="_blank">CVE-2022-1015</a> Local privilege escalation PoC for a bug in the nf_tables component of the linux kernel. More details <a href="https://blog.dbouman.nl/2022/04/02/How-The-Tables-Have-Turned-CVE-2022-1015-1016/" target="_blank">here</a>.</li>
<li><a href="https://github.com/LuxNoBulIshit/Smug_Fu3k" target="_blank">Smug_Fu3k</a> is a HTML smuggling generator.</li>
<li><a href="https://medium.com/deepfence-cloud-native-security/introducing-packetstreamer-distributed-packet-capture-for-cloud-native-platforms-3e7f9ac57ab1" target="_blank">Introducing PacketStreamer: distributed packet capture for cloud-native platforms</a>. tcpdump is perhaps my favorite debugging tool, but with the #distributed #microservices world we live in now, it can be hard to actually get packets from where you need them. PacketStreamer aims to be a universal packet forwarder to enable network visibility and debugging.</li>
<li><a href="https://github.com/arget13/DDexec" target="_blank">DDexec</a> is a technique to run binaries filelessly and stealthily on Linux by tricking dd into pwning itself (reflective injection).</li>
<li><a href="https://github.com/kris-nova/boopkit" target="_blank">boopkit</a> is a Linux eBPF backdoor over TCP. Spawn reverse shells, RCE, on prior privileged access. Less Honkin, More Tonkin.</li>
<li><a href="https://github.com/adamsvoboda/nim-loader" target="_blank">nim-loader</a> is a WIP shellcode loader in nim with EDR evasion techniques.</li>
<li><a href="https://github.com/cedowens/Dump-Chrome-Cookies" target="_blank">Dump-Chrome-Cookies</a> a modified version of CookieBro and scripts to leverage it to dump Chrome cookies. Check out the <a href="https://cedowens.medium.com/remotely-dumping-chrome-cookies-revisited-b25343257209" target="_blank">blog post</a> for more info.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/yoav-lavi/melody" target="_blank">Melody</a> is a language that compiles to regular expressions and aims to be more easily readable and maintainable.</li>
<li><a href="https://github.com/cado-security/rip_raw" target="_blank">Rip Raw</a> is a small tool to analyze the memory of compromised Linux systems.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 413 (+2)</p>
<p>Blogs monitored: 297 (+3)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
