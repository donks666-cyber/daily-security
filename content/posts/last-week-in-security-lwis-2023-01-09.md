Title: Last Week in Security (LWiS) - 2023-01-09
Date: 2023-01-09 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-01-09
Author: Erik
Summary: Korea's browser-ex problem (<a href="https://twitter.com/WPalant" target="_blank">@WPalant</a>), Prox-Ez (<a href="https://twitter.com/b1two_" target="_blank">@b1two_</a> + <a href="https://twitter.com/YofBalibump" target="_blank">@YofBalibump</a>), car hacks (<a href="https://twitter.com/samwcyo" target="_blank">@samwcyo</a>), Azure privesc (<a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>), tons of direct syscall techniques, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-01-02 to 2023-01-09.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://circleci.com/blog/january-4-2023-security-alert/" target="_blank">CircleCI security alert: Rotate any secrets stored in CircleCI (Updated Jan 7)</a>. Ouch. If you use any kind of secrets in CI (not bad by itself, depending on your threat model etc), please <a href="https://twitter.com/badsectorlabs/status/1611226303184658432" target="_blank">use canary tokens</a> so you know when you need to drop everything and rotate secrets and take a hard look at your logs.</li>
<li><a href="https://www.vice.com/en/article/wxn9vx/researchers-track-reviver-digital-license-plate-gps-location" target="_blank">Researchers Could Track the GPS Location of All of California's New Digital License Plates</a>. Because of course they can. File this under "shockingly bad idea is still bad for all the reasons we thought." For all the car hacks of 2022 check out <a href="https://samcurry.net/web-hackers-vs-the-auto-industry/" target="_blank">Web Hackers vs. The Auto Industry: Critical Vulnerabilities in Ferrari, BMW, Rolls Royce, Porsche, and More</a>.</li>
<li><a href="https://msrc-blog.microsoft.com/2022/12/29/security-update-guide-improvement-representing-hotpatch-updates/" target="_blank">Security Update Guide Improvement - Representing Hotpatch Updates</a>. You can now easily identify hotpatches for Windows Server VMs in Azure which can be applied without a reboot (feature introduced last year). Linux users heard saying "what took so long?"</li>
<li><a href="https://arxiv.org/pdf/2212.12372.pdf" target="_blank">[PDF] Factoring integers with sublinear resources on a superconducting quantum processor</a>. Researchers out of China claim to have a system where "traditional" lattice-reduction math is used to dramatically reduce the number of qbits a quantum computer needs to factor numbers (the basis of RSA). If correct, they could theoretically break 2048-bit RSA with 372 qbits (which <a href="https://newsroom.ibm.com/2022-11-09-IBM-Unveils-400-Qubit-Plus-Quantum-Processor-and-Next-Generation-IBM-Quantum-System-Two" target="_blank">IBM</a> already has). However, "<a href="https://eprint.iacr.org/2021/933" target="_blank">this destroys the RSA cryptosystem</a>" is a statement other papers have made, and so far, failed to deliver.</li>
<li><a href="https://www.usnews.com/news/top-news/articles/2023-01-05/u-s-moves-to-ban-non-compete-provisions-that-hurt-workers" target="_blank">U.S. Targets Non-Compete Clauses That Block Workers From Better Jobs</a>. A staple of any tech employment contract, the non-compete could be coming to an end.</li>
<li><a href="https://tailscale.com/blog/ssh-console/" target="_blank">Making an SSH client the hard way</a>. Your weekly reminder that the modern browser is the OS of tomorrow.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://palant.info/2023/01/09/touchen-nxkey-the-keylogging-anti-keylogger-solution/" target="_blank">TouchEn nxKey: The keylogging anti-keylogger solution</a>. Every article I read by Wladimir makes me more and more scared of any browser extension. In this case, an all-but-required extension for Korean banking can be repurposed as a keylogger easily among other scarry things.</li>
<li><a href="https://www.synacktiv.com/en/publications/escaping-from-bhyve.html" target="_blank">Escaping from bhyve</a>. A sesonsed VM escaper (<a href="http://www.phrack.org/issues/70/5.html#article" target="_blank">QEMU previously</a>) tries their hand at bhyve, FreeBSD's hypervisor, and comes away with a new VM escape. It's impressive to witness people who can point their attention at something and have impressive bugs fall out.</li>
<li><a href="https://www.synacktiv.com/en/publications/a-study-on-windows-http-authentication-part-ii.html#proxez" target="_blank">A study on Windows HTTP authentication (Part II)</a>. Kerberos over HTTP? Windows authentication options are impressive in their vastness. This is a great post for any Windows network assessor, and the <a href="https://github.com/synacktiv/Prox-Ez" target="_blank">Prox-Ez</a> tool will certainly come in handy once inside your next corporate network.</li>
<li><a href="https://trufflesecurity.com/blog/of-cors/index.html" target="_blank">Bypass firewalls with of-CORs and typo-squatting</a>. The dangers of "just clicking a link" are real in 2023, but not because your computer will get compromised (excluding browser 0day+SBX) but because your company's internal web apps are YOLOing their CORS and authentication, allowing any browser on the network to pull data. This is really neat attack that is only possible because of overpermissive internal web apps. Use <a href="https://github.com/trufflesecurity/of-cors" target="_blank">of-CORS</a> to pull off your own sweet CORS hacks.</li>
<li><a href="https://blog.fox-it.com/2022/12/28/cve-2022-27510-cve-2022-27518-measuring-citrix-adc-gateway-version-adoption-on-the-internet/" target="_blank">CVE-2022-27510, CVE-2022-27518 - Measuring Citrix ADC &amp; Gateway version adoption on the Internet</a>. The cool part of this post isn't the Citrix exploits, its the method of getting your hands on different versions of Citrix ADC images and fingerprinting the versions.</li>
<li><a href="https://thalpius.com/2023/01/06/microsoft-defender-for-identity-json-api/" target="_blank">Microsoft Defender for Identity JSON API</a>. The inner workings of the Microsoft Defender for Identity and its API can hold some secrets if you compromise a machine running a sensor. Use <a href="https://github.com/thalpius/Microsoft-Defender-for-Identity-API-Fiddler" target="_blank">Microsoft-Defender-for-Identity-API-Fiddler</a> to play with it.</li>
<li><a href="https://labs.nettitude.com/blog/cve-2022-25026-cve-2022-25027-vulnerabilities-in-rocket-trufusion-enterprise/" target="_blank">CVE-2022-25026 &amp; CVE-2022-25027: Vulnerabilities in Rocket TRUfusion Enterprise</a>. Some classic web app vulnerabilities in this post.</li>
<li><a href="https://blog.nviso.eu/2023/01/04/dettct-automate-your-detection-coverage-with-dettectinator/" target="_blank">DeTT&amp;CT: Automate your detection coverage with dettectinator</a> . This post introduces a new tool, dettectinator, which is a framework that helps blue teams in using MITRE ATT&amp;CK to score and compare data log source quality, visibility coverage, detection coverage and threat actor behaviors.</li>
<li><a href="https://posts.specterops.io/passwordless-persistence-and-privilege-escalation-in-azure-98a01310be3f" target="_blank">Passwordless Persistence and Privilege Escalation in Azure</a>. TIL that Azure comes with its own privesc to Global Admin. Neat.</li>
<li><a href="https://www.wiz.io/blog/lateral-movement-risks-in-the-cloud-and-how-to-prevent-them-part-2-from-k8s-clust" target="_blank">Lateral movement risks in the cloud and how to prevent them - Part 2: from compromised container to cloud takeover</a>. What can you do once you land in a prod pod? Depends on the cloud, but probably a lot.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/romainthomas/iCDump/" target="_blank">iCDump</a>. A Modern Objective-C Class Dump. Blog <a href="https://www.romainthomas.fr/post/23-01-icdump/" target="_blank">here</a>.</li>
<li><a href="https://github.com/D1rkMtr/UnhookingPatch" target="_blank">UnhookingPatch</a> - Bypass EDR Hooks by patching NT API stub, and resolving SSNs and syscall instructions at runtime.</li>
<li><a href="https://github.com/Maldev-Academy/HellHall" target="_blank">HellHall</a> is a combination of HellsGate and indirect syscalls.</li>
<li><a href="https://github.com/DallasFR/WalkerGate" target="_blank">WalkerGate</a> is a method to take syscall with memory parsing of ntdll.</li>
<li><a href="https://gitlab.com/Zer1t0/zsyscall" target="_blank">zsyscall</a> is an implementation of the Hell's Gate VX technique. The main difference with the original implementation is the use of the zsyscall procedure instead of HellsGate and HellDescent for using syscalls.</li>
<li><a href="https://github.com/zdhenard42/SOC-Multitool" target="_blank">SOC-Multitool</a> - A free and open source tool to aid in SOC investigations!</li>
<li><a href="https://github.com/weak1337/Alcatraz" target="_blank">Alcatraz</a> is a x64 binary obfuscator that is able to obfuscate various different pe formats.</li>
<li><a href="https://github.com/0xAkashsky/sub-scout" target="_blank">sub-scout</a> is a simple bash script to automate your inital recon and extend your attack surface using popular tools made by infosec community.</li>
<li><a href="https://github.com/EspressoCake/MITRE_ATTACK_CLI" target="_blank">MITRE_ATTACK_CLI</a> - CLI Search for Security Operators of MITRE ATT&amp;CK URLs.</li>
<li><a href="https://github.com/DevSecOpsDocs/nuclearpond" target="_blank">nuclearpond</a> is a utility leveraging Nuclei to perform internet wide scans for the cost of a cup of coffee.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.gosecure.net/blog/2022/12/23/a-new-pyrdp-release-the-rudolph-desktop-protocol/" target="_blank">A New PyRDP Release: The Rudolph Desktop Protocol!</a>. The gosecure RSS feed was slow on this one?</li>
<li><a href="https://github.com/redhuntlabs/kubestalk" target="_blank">KubeStalk</a> discovers Kubernetes and related infrastructure based attack surface from a black-box perspective.</li>
<li><a href="https://github.com/praetorian-inc/NTLMRecon" target="_blank">NTLMRecon</a> - A tool for performing light brute-forcing of HTTP servers to identify commonly accessible NTLM authentication endpoints.</li>
<li><a href="https://github.com/activecm/smudge" target="_blank">smudge</a> - Passive OS detection based on SYN packets without Transmitting any Data</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 422 (+0)</p>
<p>Blogs monitored: 330 (+0)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
