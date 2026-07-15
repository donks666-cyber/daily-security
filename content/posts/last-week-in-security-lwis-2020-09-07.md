Title: Last Week in Security (LWiS) - 2020-09-07
Date: 2020-09-08 22:15
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-09-07
Author: Erik
Summary: Remote SAM dumping in .NET by <a href="https://mobile.twitter.com/G0ldenGunSec" target="_blank">@G0ldenGunSec</a>, Using Yara offensively by <a href="https://twitter.com/_batsec_" target="_blank">@_batsec_</a>, Custom DLL injection in CobaltStrike by <a href="https://twitter.com/tomcarver_" target="_blank">@tomcarver_</a>, a C# Chrome cookie cloner from <a href="https://twitter.com/buffaloverflow" target="_blank">@buffaloverflow</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-08-31 to 2020-09-07.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://developer.apple.com/news/?id=kuswih5l" target="_blank">Easily create web extensions for Safari</a>. Not a great title, but the message is that Safari is getting the standard WebExtensions API used by Chrome (and all Chrome variants) and Firefox. Develop your browser extension once, deploy to every major browser!</li>
<li><a href="https://www.docker.com/blog/scaling-docker-to-serve-millions-more-developers-network-egress/" target="_blank">Scaling Docker to Serve Millions More Developers: Network Egress</a>. Docker has had a rough few years and they are trying to stop the bleeding by limiting free accounts to 100 pulls per 6 hours (200 per 6 hours if authenticated).</li>
<li><a href="https://xtraining.kaspersky.com/" target="_blank">Online Cybersecurity Training for Experts</a>. Kaspersky is now offering online YARA rule creation training, with more courses on the way.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.dylan.codes/pwning-windows-event-logging/" target="_blank">Pwning Windows Event Logging with YARA rules</a>. This project allows for offensive operators to selectively mute logging using Yara rules in memory. It works by injecting a hook into the ETW event callback function and using Yara to scan the contents of every event to determine if it should be dropped or not. <a href="https://github.com/bats3c/EvtMute" target="_blank">EvtMute</a> contains all the code and example Yara rules.</li>
<li><a href="https://blog.christophetd.fr/privilege-escalation-in-aws-elastic-kubernetes-service-eks-by-compromising-the-instance-role-of-worker-nodes/" target="_blank">Privilege Escalation in AWS Elastic Kubernetes Service (EKS) by compromising the instance role of worker nodes</a>. AWS account-wide denial of service and enumeration is accessible by only having compromised a single, underprivileged pod in the cluster. The AWS accounts in question come by default when spinning up an EKS cluster. The post includes remediation steps to block the AWS metadata service access from pods to prevent this attack.</li>
<li><a href="https://www.mnemonic.no/blog/abusing-dynamic-groups-in-azure/" target="_blank">Abusing dynamic groups in Azure AD for privilege escalation</a>. Putting AD in the cloud introduced new features, and new potential vulnerabilities, in this case the ability to abuse dynamic groups to access other accounts or modify attributes. If AD Connect Sync is in use, on-prem ADs can be affected as well.</li>
<li><a href="https://www.trustedsec.com/blog/so-you-got-access-to-a-nix-system-now-what/" target="_blank">So, You Got Access to a *nix system… Now What?</a>. This quick post is a basic overview, but may contain a new script or command you didn't previously know about.</li>
<li><a href="https://x64sec.sh/custom-dll-injection-with-cobalt-strike/" target="_blank">Custom DLL injection with Cobalt Strike's Beacon Object Files</a>. Cobalt Strike is a great C2 platform, but the fact that it is popular means it will be detected without some work to modify it. In this post Tom Carver works through building a custom DLL injector using the new Beacon Object File spec from the 4.1 release.</li>
<li><a href="https://www.gosecure.net/blog/2020/09/03/wsus-attacks-part-1-introducing-pywsus/" target="_blank">WSUS Attacks Part 1: Introducing PyWSUS</a>. Scary things happen when you can Man-in-the-middle connections. In this post, ARP spoofing is used to intercept and respond to a Windows update request which allows for arbitrary code execution as SYSTEM if the system is not using HTTPS for WSUS. Video <a href="https://youtu.be/TkrnQEg7SYI" target="_blank">here</a>, code <a href="https://github.com/GoSecure/pywsus" target="_blank">here</a>.</li>
<li><a href="https://github.com/bytecode77/living-off-the-land" target="_blank">living-off-the-land</a> combines some tricks to achieve persistence with two registry writes (semi-hidden) and no files on disk.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/G0ldenGunSec/SharpSecDump" target="_blank">SharpSecDump</a> is a .Net port of the remote SAM + LSA Secrets dumping functionality of impacket's secretsdump.py. By default runs in the context of the current user, but can use alternate credentials supplied on the command line. Note: this doesn't have DCSync functionality yet so no AD dumping - use <a href="https://github.com/b4rtik/SharpKatz" target="_blank">SharpKatz</a> for that.</li>
<li><a href="https://www.solomonsklash.io/seaside-bishop.html" target="_blank">SeasideBishop: A C port of b33f’s UrbanBishop shellcode injector</a>. AV/EDR detecting your standard injection methods? Try this latest iteration of the *Bishop series which uses some tricks and APC queuing to inject shellcode into a process. Code <a href="https://github.com/SolomonSklash/SeasideBishop" target="_blank">here</a>.</li>
<li><a href="https://www.zerodayinitiative.com/blog/2020/9/1/cve-2020-7460-freebsd-kernel-privilege-escalation" target="_blank">CVE-2020-7460: FreeBSD Kernel Privilege Escalation</a>. A rare FreeBSD privilege escalation for any 64 bit kernel since 2014. PoC <a href="https://github.com/thezdi/PoC/blob/master/CVE-2020-7460/CVE-2020-7460.c" target="_blank">here</a>.</li>
<li><a href="https://github.com/blacklanternsecurity/TREVORspray" target="_blank">TREVORspray</a> is a featureful Python O365 sprayer based on MSOLSpray which uses the Microsoft Graph API that can use SSH hosts to proxy requests.</li>
<li><a href="https://github.com/0xnobody/vmpdump">vmpdump</a> is yet another (this makes 3, see <a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2020-08-17.html">LWiS-2020-08-17</a>) VMProtect deobfuscator.</li>
<li><a href="https://www.synacktiv.com/publications/ubuntu-ppps-cve-2020-15704-wrap-up" target="_blank">Ubuntu ppp's CVE-2020-15704 wrap-up</a>. On certain Ubuntu machines from 12.04 to 20.04 (KVM kernel builds) that don't have /dev/ppp, modprobe environment variables can be used for arbitrary file read.</li>
<li><a href="https://watchcom.no/nyheter/nyhetsarkiv/uncovers-cisco-jabber-vulnerabilities/" target="_blank">Watchcom Security Group uncovers Cisco Jabber vulnerabilities</a>. Cisco Jabber is often seen in enterprise environments for team collaboration and is another good example of how using Electron/Chromium based apps can turn a simple XSS into an RCE.</li>
<li><a href="https://googleprojectzero.blogspot.com/p/rca-cve-2020-0986.html" target="_blank">CVE-2020-0986: Windows splwow64 Untrusted Pointer Dereference</a>. Google Project Zero drops this Windows privilege escalation (patched 2020-06-09) that was reported by Kaspersky Lab who found it being used in the wild.</li>
<li><a href="https://github.com/rxwx/chlonium" target="_blank">chlonium</a> is a C# application designed for cloning Chromium Cookies. The unique feature here is the utility to allow the easy importing of Chrome cookies into a second browser. Demo <a href="https://vimeo.com/452632559?quality=1080p" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/SomeKirill/wordlist_generator" target="_blank">wordlist_generator</a> generates wordlists with unique words with techniques mentioned in tomnomnom's report <a href="https://www.youtube.com/watch?v=W4_QCSIujQ4" target="_blank">"Who, What, Where, When"</a>. It takes URLs from gau and splits them to get words in URLs. Then it requests each URL to fetch all words. Finally, wordlist_generator removes from wordlist everything from "denylists" directory files to keep only unique words, which you can use for domain, directory, parameter, vhosts, etc bruteforcing.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
