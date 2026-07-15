Title: Last Week in Security (LWiS) - 2025-03-03
Date: 2025-03-03 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2025-03-03
Author: Erik
Summary: Ligolo-MP (<a href="https://x.com/ttpreport" target="_blank">@ttpreport</a>), Bybit hack via CI (<a href="https://x.com/adnanthekhan" target="_blank">@adnanthekhan</a>), FindGPPPasswords (<a href="https://x.com/podalirius_" target="_blank">@podalirius_</a>), ComDotNetExploit (<a href="https://x.com/T3nb3w" target="_blank">@T3nb3w</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2025-02-25 to 2025-03-03.</p>
<section id="news">
<h2>News</h2>
<aside class="m-block m-success">
<h3><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Learn Azure and On-Prem Red Teaming</a> <span class="m-label m-flat m-success">Sponsored</span></h3>
<p>Start your Red Ream training with us! Altered Security offers multiple Red Team course with affordable and enterprise-like hands-on labs. Each course comes with an industry-recognized certification. We are the creators of the Certified Red Team Professional (CRTP), CRTE, CARTP and more. Our courses and labs are designed by experts who have more than a decade's experience of training and speaking at Black Hat USA, DEF CON and other respected conferences.</p>
<p>Join more than 40K professionals from 130+ countries. <strong><a href="https://www.alteredsecurity.com/online-labs" style="color: #3bd267;" target="_blank">Sign up now!</a></strong></p>
</aside><ul>
<li><a href="https://adnanthekhan.com/2025/02/27/not-so-safewallet-github-actions-risks-impacting-safes-frontend/" target="_blank">(Not So) Safe{Wallet}: GitHub Actions Risks Impacting Safe’s Frontend</a> - The record setting cryptocurrency theft from last week may come down to a complex continuous integration/continuous deployment abuse from a compromised developer's workstation.</li>
<li><a href="https://www.schneier.com/blog/archives/2025/02/an-icloud-backdoor-would-make-our-phones-less-safe.html" target="_blank">UK Demanded Apple Add a Backdoor to iCloud</a> - A good argument against the UK backdoor of iCloud.</li>
<li><a href="https://gitlab-com.gitlab.io/gl-security/security-tech-notes/threat-intelligence-tech-notes/malicious-browser-extensions-feb-2025/" target="_blank">Tech Note - Malicious browser extensions impacting at least 3.2 million users</a> - The browser is the new OS, and it's getting attacked.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://ttp.report/tools/2025/03/03/ligolo-mp-automagic-and-gui.html" target="_blank">Ligolo-MP 2.0: automagic &amp; GUI</a> - New ligolo-NG alternative with a GUI. The "Effortless multiplayer setup" looks pretty cool.</li>
<li><a href="https://medium.com/@WaterBucket/understanding-deferred-procedure-calls-dpcs-in-windows-ecd138292883" target="_blank">Understanding Deferred Procedure Calls (DPCs) for Windows Vulnerability Research &amp; Exploit Development</a> - When listening to podcast leads to interesting windows internals research. Deferred Procedure Calls (DPCs) are not a common topic for the common infosec community. Good read.</li>
<li><a href="https://www.synacktiv.com/en/publications/taking-the-relaying-capabilities-of-multicast-poisoning-to-the-next-level-tricking" target="_blank">Taking the Relaying Capabilities of Multicast Poisoning to the Next Level: Tricking Windows SMB Clients Into Falling Back to Webdav</a> - With more and more organizations using SMB signing which prevents relaying, being able to get a client to fallback to Webdav opens up new possibilities for relaying attacks in Windows networks.</li>
<li><a href="https://neodyme.io/en/blog/com_hijacking_4/" target="_blank">The Key to COMpromise - Writing to the Registry (again), Part 4</a> - The final installment of this excellent series focuses on getting SYSTEM from Bitdefender Total Security and how to use COM for denial of service attacks against security software.</li>
<li><a href="https://practicalsecurityanalytics.com/bypassing-amsi-and-evading-av-detection-with-specterinsight/" target="_blank">Bypassing AMSI and Evading AV Detection with SpecterInsight</a> - Padding with legitimate scripts a technique not often discussed but quite effective.</li>
<li><a href="https://gfw.report/publications/ndss25/en/" target="_blank">Wallbleed: A Memory Disclosure Vulnerability in the Great Firewall of China</a> - "We present Wallbleed, a buffer over-read vulnerability that existed in the DNS injection subsystem of the Great Firewall of China. Wallbleed caused certain nation-wide censorship middleboxes to reveal up to 125 bytes of their memory when censoring a crafted DNS query. It afforded a rare insight into one of the Great Firewall’s well-known network attacks, namely DNS injection, in terms of its internal architecture and the censor’s operational behaviors." A rare look behind the curtain.</li>
<li><a href="https://en.r-tec.net/r-tec-blog-bypass-amsi-in-2025.html" target="_blank">Bypass AMSI in 2025</a> - This post will shed some light on what's behind AMSI and how you can still effectively bypass it - more than four years later.</li>
<li><a href="https://kibty.town/blog/todesktop/" target="_blank">How to gain code execution on millions of people and hundreds of popular apps</a> - Firebase permissions strike again. When a product is so hard to get right, perhaps it's the products fault.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/seahop/clio" target="_blank">Clio</a> - Logging tool intended for red team usage.</li>
<li><a href="https://github.com/rb-x/penflow" target="_blank">penflow</a> - 🎯 Visualize Your Security Testing &amp; Analysis Journey.</li>
<li><a href="https://github.com/faizann24/baby-naptime" target="_blank">baby-naptime</a> - A very simple open source implementation of Google's Project Naptime.</li>
<li><a href="https://github.com/0xRedpoll/WhatsAppKeyBOF" target="_blank">WhatsAppKeyBOF</a> - A BOF to retrieve decryption keys for WhatsApp Desktop and a utility script to decrypt the databases.</li>
<li><a href="https://github.com/MHaggis/PowerShell-Hunter" target="_blank">PowerShell-Hunter</a> - PowerShell tools to help defenders hunt smarter, hunt harder.</li>
<li><a href="https://github.com/T3nb3w/ComDotNetExploit" target="_blank">ComDotNetExploit</a> - A C++ proof of concept demonstrating the exploitation of Windows Protected Process Light (PPL) by leveraging COM-to-.NET redirection and reflection techniques for code injection. This PoC showcases bypassing code integrity checks and loading malicious payloads in highly protected processes such as LSASS. Based on research from James Forshaw.</li>
<li><a href="https://github.com/jtesta/k8s_spoofilizer" target="_blank">k8s_spoofilizer</a> - Creates Kubernetes Golden Tickets through ServiceAccount token forging and user certificate forging. Read more at: <a href="https://www.positronsecurity.com/blog/2025-02-26-kubernetes-golden-tickets/" target="_blank">Kubernetes Golden Tickets</a></li>
<li><a href="https://github.com/RobertWesner/titryes" target="_blank">titryes</a> - Run Dockerized web browsers from other operating systems on Linux.</li>
<li><a href="https://github.com/blacklanternsecurity/webcap" target="_blank">webcap</a> - An ultra lightweight web screenshot tool with advanced DOM analysis features.</li>
<li><a href="https://github.com/p0dalirius/FindGPPPasswords" target="_blank">FindGPPPasswords</a> - A cross-platform tool to find and decrypt Group Policy Preferences passwords from the SYSVOL share using low-privileged domain accounts.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://yprobe.loworbitsecurity.com/" target="_blank">yProbe</a> - Kubernetes YAML Manifest Sanity Checker</li>
<li><a href="https://mitogen.networkgenomics.com/ansible_detailed.html" target="_blank">Mitogen for Ansible</a> - Mitogen for Ansible is a completely redesigned UNIX connection layer and module runtime for Ansible.</li>
<li><a href="https://www.interviewcoder.co/" target="_blank">Interview Coder</a> is an invisible AI to solve any coding problem.</li>
<li><a href="https://www.youtube.com/watch?v=h9Z4oGN89MU" target="_blank">How do Graphics Cards Work? Exploring GPU Architecture</a> - Very well done video breaking down what a graphics card is at the physical level.</li>
<li><a href="https://github.com/0xAwali/WebSocketChecker" target="_blank">WebSocketChecker</a> - Burp suite extension to find sensitive information by checking incoming text OR binary websocket messages.</li>
<li><a href="https://github.com/yusuf-musleh/mmar" target="_blank">mmar</a> - mmar is a zero-dependency, self-hostable, cross-platform HTTP tunnel that exposes your localhost to the world on a public URL. Written in Go.</li>
<li><a href="https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice#demo" target="_blank">Conversational voice demo</a> - This demo is worth giving microphone access for. AI is getting really close to "Her" levels. Imagine this but backed by GPT4.5.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>X accounts monitored: 444 (+0)</p>
<p>Blogs monitored: 406 (+1)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions, comments, or want to sponsor LWiS?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
<p>Mastodon: <a href="https://infosec.exchange/@badsectorlabs" target="_blank">@badsectorlabs@infosec.exchange</a></p>
<p>Bluesky: <a href="https://bsky.app/profile/badsectorlabs.com" target="_blank">@badsectorlabs.com</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.</p>
</section>
