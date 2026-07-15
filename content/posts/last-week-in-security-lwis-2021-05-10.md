Title: Last Week in Security (LWiS) - 2021-05-10
Date: 2021-05-11 17:30
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-05-10
Author: Erik
Summary: Full DarkHotel exploit ⛓️ (<a href="https://twitter.com/_forrestorr" target="_blank">@_ForrestOrr</a>), DomainBorrowing (<a href="https://twitter.com/md5_salt" target="_blank">@md5_salt</a>), WinPmem to dump LSASS (<a href="https://twitter.com/TheXC3LL" target="_blank">@TheXC3LL</a>), Twitter Tip Jar fail (<a href="https://twitter.com/RachelTobac" target="_blank">@RachelTobac</a>), the reasoning behind DripLoader (<a href="https://twitter.com/_lpvoid" target="_blank">@_lpvoid</a>), .NET + NTFS tricks (<a href="https://twitter.com/G0ldenGunSec" target="_blank">@G0ldenGunSec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-05-03 to 2021-05-10.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.colpipe.com/news/press-releases/media-statement-colonial-pipeline-system-disruption" target="_blank">Media Statement Update: Colonial Pipeline System Disruption</a>. The gasoline pipeline that runs up the east coast of the US is partially shut down and is operating on manual control after a DarkSide ransomware attack. After large media attention, the DarkSide crew released a statement that <a href="https://www.vice.com/en/article/bvzzez/colonial-pipeline-hackers-statement-darkside" target="_blank">"our goal is to make money, and not creating problems for society."</a> Perhaps choose a line of work that doesn't involve ransoming data?</li>
<li><a href="https://www.icta.mu/docs/2021/Social_Media_Public_Consultation.pdf" target="_blank">Consultation Paper on proposed amendments to the ICT Act for regulating the use and addressing the abuse and misuse of Social Media in Mauritius</a>. The small Indian Ocean nation is proposing to "segregate... all incoming and outgoing internet traffic in Mauritius, social media traffic, which will then need to be decrypted, re-encrypted and archived for inspection purposes as and when required." Man-in-the-middle-ing a whole country is easier when there are only four fiber lines in and out, until <a href="https://www.starlink.com/" target="_blank">Starlink</a> arrives. This will require all citizen to install a new Certificate Authority - a process few understand and will normalize a dangerous process leaving the door open to malware and scammers.</li>
<li><a href="https://kb.pulsesecure.net/pkb_mobile#article/l:en_US/SA44784/s" target="_blank">SA44784 - 2021-04: Out-of-Cycle Advisory: Multiple Vulnerabilities Resolved in Pulse Connect Secure 9.1R11.4</a>. Nothing like a CVSS 10.0 remote unauthenticated code execution vulnerability in your VPN to wake you out of the normal vulnerability reviews. This one is already being exploited in the wild.</li>
<li><a href="https://www.qualys.com/2021/05/04/21nails/21nails.txt" target="_blank">21Nails: Multiple vulnerabilities in Exim</a>. Some serious issues discovered in the popular Exim mail server, including a chain that could allow for unauthenticated RCE as root. Exim has released an update, which <a href="https://us-cert.cisa.gov/ncas/current-activity/2021/05/07/exim-releases-security-update" target="_blank">CISA is pushing</a>. PoC video <a href="https://vimeo.com/544783362" target="_blank">here</a>.</li>
<li><a href="https://twitter.com/RachelTobac/status/1390409874006183936" target="_blank">Twitter Tip Jar reveals address of tipper</a>. PayPal, like parent company eBay, is stuck in the early 2000's and coasting on market dominance. It's surprising no one at Twitter caught this before launch.</li>
<li><a href="https://gynvael.coldwind.pl/?id=733" target="_blank">Feral Terror vulnerability (some NETGEAR smart switches)</a>. Update those Netgear switches before the PoC drops on 2021-05-17!</li>
<li><a href="https://labs.sentinelone.com/cve-2021-21551-hundreds-of-millions-of-dell-computers-at-risk-due-to-multiple-bios-driver-privilege-escalation-flaws/" target="_blank">CVE-2021-21551- Hundreds Of Millions Of Dell Computers At Risk Due to Multiple BIOS Driver Privilege Escalation Flaws</a>. A driver shipped with most (all?) Dell Windows computers contained 5 flaws, 4 of which can be exploit for local elevation of privileges. PoC is being withheld until 2021-06-01 to allow patches to propigate.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://adepts.of0x.cc/physical-graffiti-lsass/" target="_blank">A physical graffiti of LSASS: getting credentials from physical memory for fun and learning</a>. With all the modern protections on memory access, what if you just used "physical" memory access to get secrets from LSASS? This post shows how the <a href="https://github.com/Velocidex/WinPmem" target="_blank">WinPmem</a> driver can do just that. PoC code <a href="https://github.com/Adepts-Of-0xCC/SnoopyOwl" target="_blank">here</a>.</li>
<li><a href="https://www.vice.com/en/article/7kvvbb/argyle-payroll-login-phishing" target="_blank">'Phishing' Sites Buying Workplace Login Details Linked to Well-Funded Startup</a>. Stop phishing with tricks and just buy access? Bold and seemingly effective.</li>
<li><a href="https://krebsonsecurity.com/2021/05/malicious-office-365-apps-are-the-ultimate-insiders/" target="_blank">Malicious Office 365 Apps Are the Ultimate Insiders</a>. In the age of the cloud, a 3rd-party "app" for your cloud is the ultimate persistence technique.</li>
<li><a href="https://blog.redxorblue.com/2021/05/assemblylie-using-transactional-ntfs.html" target="_blank">Assembly.Lie – Using Transactional NTFS and API Hooking to Trick the CLR into Loading Your Code “From Disk”</a>. Using some NTFS tricks, you can make your CLR assemblies appear to be loaded from "legitimate" looking paths on disk, like system32. For PoC code check out <a href="https://github.com/G0ldenGunSec/SharpTransactedLoad" target="_blank">SharpTransactedLoad</a>.</li>
<li><a href="https://public.cnotools.studio/bring-your-own-vulnerable-kernel-driver-byovkd/exploits/data-only-attack-neutralizing-etwti-provider" target="_blank">Data Only Attack: Neutralizing EtwTi Provider</a>. While this method requires a driver signing bypass (or Arbitrary Ring 0 R/W), as more EDR vendors move to the kernel this is the future of anti-detection engineering.</li>
<li><a href="https://blog.redbluepurple.io/offensive-research/bypassing-injection-detection" target="_blank">Bypassing EDR real-time injection detection logic</a>. This is the post that explains the reasoning behind last week's <a href="https://github.com/xinbailu/DripLoader" target="_blank">DripLoader</a> release.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/forrest-orr/DoubleStar" target="_blank">DoubleStar</a> is a personalized/enhanced re-creation of the Darkhotel "Double Star" APT exploit chain with a focus on Windows 8.1 and mixed with some custom techniques. While this exploit chain makes use of two (now patched) 0day exploits, it also contains an elevation of privilege technique which is still as of 2021-05-10 not patched, and remains feasible for integration into future attack chains today.</li>
<li><a href="https://posts.specterops.io/introducing-mystikal-4fbd2f7ae520" target="_blank">Introducing Mystikal</a>. As more small and even large businesses adopt macOS, red teams are starting to focus more on the previously obscure platform. Mystikal is an initial access payload generator for macOS that includes: pkg installer with JavaScript, Microsoft Office Macros, and Armed "PDFs" (apps). Code <a href="https://github.com/D00MFist/Mystikal" target="_blank">here</a>.</li>
<li><a href="https://github.com/cedowens/keygrabber" target="_blank">keygrabber</a> is a script for grabbing keys from a Linux host. Useful during red team exercises to quickly help assess what access to a Linux host can lead to.</li>
<li><a href="https://github.com/rajiv2790/FalconEye" target="_blank">FalconEye</a> is a windows endpoint detection software for real-time process injections. It is a kernel-mode driver that aims to catch process injections as they are happening (real-time). Since FalconEye runs in kernel mode, it provides a stronger and reliable defense against process injection techniques that try to evade various user-mode hooks. Add this to your detection lab and see if you can bypass it!</li>
<li><a href="https://github.com/Dliv3/DomainBorrowing" target="_blank">DomainBorrowing</a> is a <a href="https://github.com/cobbr/Covenant" target="_blank">Covenant</a> implementation of the evolution of my talk on <a href="https://youtu.be/TDg092qe50g" target="_blank">Domain Hiding</a> (since crippled by Cloudflare). Using some smaller CDNs it's possible to "borrow" a wildcard certificates if you register a nonexistent subdomain with them. Like Domain Hiding, this technique likely has a short shelf life but is really great research!</li>
<li><a href="https://github.com/lateralusd/lateralus" target="_blank">lateralus</a> is a terminal based phishing campaign tool with template support. Could be useful for quick campaigns where you don't need the full power of something like <a href="https://getgophish.com/" target="_blank">Gophish</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/MythicAgents/poseidon" target="_blank">poseidon</a> is a fully featured macOS <a href="https://github.com/its-a-feature/Mythic" target="_blank">Mythic</a> implant with some Linux functionality as well.</li>
<li><a href="https://github.com/metacall/core" target="_blank">metacall/core</a> allows calling functions, methods or procedures between multiple programming languages. The ability to glue together multiple languages into a single solution without much overhead is very cool.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
