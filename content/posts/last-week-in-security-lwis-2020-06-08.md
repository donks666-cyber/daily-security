Title: Last Week in Security (LWiS) - 2020-06-08
Date: 2020-06-08 20:35
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-06-08
Author: Erik
Summary: A new Windows C implant from <a href="https://twitter.com/_batsec_" target="_blank">@_batsec_</a>, a tool to detect .NET in memory by <a href="https://twitter.com/domchell" target="_blank">@domchell</a>, big updates to Covenant from <a href="https://twitter.com/cobbr_io" target="_blank">@cobbr_io</a>, a new process injection technique from <a href="https://twitter.com/0x00dtm" target="_blank">@0x00dtm</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-06-01 to 2020-06-08.
No MITRE ATT&amp;CK techniques are in brackets this week, too much content!</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blog.talosintelligence.com/2020/06/vuln-spotlight-zoom-code-execution-june-2020.html" target="_blank">Vulnerability Spotlight: Two vulnerabilities in Zoom could lead to code execution</a>. Normally I would jump on the chance to shame Zoom, but these vulnerability are pretty weak - a path traversal that can drop an empty exe, or a code snippet that could drop an exe that requires a user to click to save. These are legitimate vulnerabilities that should be patched (and were in just 5 days and a month respectively), but not a 8.5/8.0 CVSS score that Talos gave them. Judge for yourself - <a href="https://talosintelligence.com/vulnerability_reports/TALOS-2020-1055" target="_blank">TALOS-2020-1055</a> and <a href="https://talosintelligence.com/vulnerability_reports/TALOS-2020-1056" target="_blank">TALOS-2020-1056</a>.</li>
<li><a href="https://www.theguardian.com/technology/2020/jun/03/zoom-privacy-law-enforcement-technology-yuan" target="_blank">Zoom to exclude free calls from end-to-end encryption to allow FBI cooperation</a>. Normally cooperation with the FBI is assumed but Eric Yuan, Zoom's CEO said in a call with analysts, "we also want to work together with FBI, with local law enforcement in case some people use Zoom for a bad purpose." At least he is being open about it.</li>
<li><a href="https://www.androidauthority.com/android-wallpaper-crash-1124577/" target="_blank">Wallpaper crash explained: Here’s how a simple image can soft-brick phones</a>. We've seen comedy bugs like this in iOS <a href="https://www.theverge.com/2020/4/24/21234191/apple-iphone-crash-text-bug-ios-13-problem" target="_blank">before</a> but this is the first for android in a long time. A good reminder that despite how reliable modern software seems, it's all susceptible to silly bugs that can bring it all down.</li>
<li><a href="https://www.mozilla.org/en-US/firefox/77.0.1/releasenotes/" target="_blank">Disabled automatic selection of DNS over HTTPS providers during a test to enable wider deployment in a more controlled way</a>. Firefox steps back their DNS over HTTPS push fearing a possible DDoS against providers when all users update in a short timespan. Interesting to see a major browser take a step back like this. The default provider is Cloudflare, which seems like the most qualified entity to handle a large influx of traffic.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://itm4n.github.io/chimichurri-reloaded/" target="_blank">Chimichurri Reloaded - Giving a Second Life to a 10-year old Windows Vulnerability</a> brings back <a href="https://www.cvedetails.com/cve/CVE-2010-2554/" target="_blank">CVE-2010-2554</a> (Vista!) by having Windows authenticate to itself (a la *potato exploits). Another great one from <a href="https://twitter.com/itm4n" target="_blank">@itm4n</a>.</li>
<li><a href="https://ired.team/offensive-security/defense-evasion/retrieving-ntdll-syscall-stubs-at-run-time" target="_blank">Retrieving ntdll Syscall Stubs from Disk at Run-time</a> is an interesting technique to keep windows syscalling flexible. However, it may increase the detection rate of your tool, so be sure to test before abandoning static syscall tables. For a different take on the same technique, check out <a href="https://github.com/am0nsec/HellsGate" target="_blank">HellsGate</a> (obligatory C# version <a href="https://github.com/am0nsec/SharpHellsGate" target="_blank">here</a>). Want more syscall information from this week? Check out <a href="https://www.solomonsklash.io/syscalls-for-shellcode-injection.html" target="_blank">Using Syscalls to Inject Shellcode on Windows</a>.</li>
<li><a href="https://github.com/aronskaya/smjobbless" target="_blank">smjobbless</a> is a showcase for launching Privileged Helper via SMJobBless() and communicating with it using XPC. For more information on XPC, see LWiS 2020-05-18 (<a href="https://rekken.github.io/2020/05/14/Security-Flaws-in-Adobe-Acrobat-Reader-Allow-Malicious-Program-to-Gain-Root-on-macOS-Silently/" target="_blank">Adobe LPE</a>) and 2020-03-23 (<a href="https://www.securing.biz/en/abusing-securing-xpc-in-macos-apps/index.html" target="_blank">Abusing &amp; Securing XPC in macOS apps</a>).</li>
<li><a href="https://www.mdsec.co.uk/2020/06/detecting-and-advancing-in-memory-net-tradecraft/" target="_blank">Detecting and Advancing In-Memory .NET Tradecraft</a>. With all the .NET tools released over the past year+, defenders needed a break. <a href="https://twitter.com/domchell" target="_blank">@domchell</a> discusses methods of detecting in memory .NET and provides a proof of concept <a href="https://github.com/dmchell/Sniper" target="_blank">tool</a> to do so.</li>
<li><a href="https://github.com/DefensiveOrigins/APT06202001" target="_blank">Applied Purple Teaming</a> is the courseware and labs for <a href="https://twitter.com/DefensiveOGs" target="_blank">@DefensiveOGs</a>'s Applied Purple Teaming: Infrastructure, Threat Optics, and Continuous Improvement 4 hour course. Some great content, and good scripts to use as inspiration for lab setup.</li>
<li><a href="https://medium.com/@shantanukhande/red-team-how-to-embed-golang-tools-in-c-e269bf33876a" target="_blank">Red Team: How to embed Golang tools in C#</a> if you've been writing your tools in Go but still want to take advantage of all the great C# implants/loaders, this blog will show you how to wrap your Go and load it in memory with C#!</li>
<li><a href="https://medium.com/@BreizhZeroDayHunters/when-its-not-only-about-a-kubernetes-cve-8f6b448eafa8" target="_blank">When it’s not only about a Kubernetes CVE…</a> When everything has a web API, a server side request forgery (SSRF) bug can be an infrastructure bug.</li>
<li><a href="https://byteraptors.github.io/windows/exploitation/2020/06/03/exploitingcve2019-1458.html" target="_blank">The WizardOpium LPE: Exploiting CVE-2019-1458</a> explores an older kernel exploit from December 2019. This is a great starting point if you are interested in Windows kernel exploitation.</li>
<li><a href="https://securityjunky.com/guide-to-setting-up-android-pentesting-lab/" target="_blank">Guide to Setting Up Android Pentesting Lab</a> Many developers consider mobile applications "safer" than desktop applications due to the hurdle of getting access to a phone (i.e. jailbreak, root, etc) for testing. This post gives a step-by-step walkthrough on setting up a virtual Android lab to start exploring.</li>
<li><a href="https://undev.ninja/nina-x64-process-injection/" target="_blank">NINA: x64 Process Injection</a> is a new experimental process injection technique with a hard restriction on the usage of common and "dangerous" functions, i.e. WriteProcessMemory, VirtualAllocEx, VirtualProtectEx, CreateRemoteThread, NtCreateThreadEx, QueueUserApc, and NtQueueApcThread. PoC code <a href="https://github.com/NtRaiseHardError/NINA" target="_blank">here</a>.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/cwinfosec/epic_shell" target="_blank">epic_shell</a> is a new PHP webshell with encryption that shows a decoy 404 page for anyone browsing it without the proper key. <cite>shell_exec</cite> is required for proper functionality.</li>
<li><a href="https://github.com/chompie1337/SMBGhost_RCE_PoC" target="_blank">SMBGhost_RCE_PoC</a> is the remote version of the LPE released a few months ago that works against Windows 10 1903 (SMBv3 compression). Full technical writeup <a href="https://ricercasecurity.blogspot.com/2020/04/ill-ask-your-body-smbghost-pre-auth-rce.html" target="_blank">here</a>.</li>
<li><a href="https://github.com/aaronsvk/CVE-2020-3956/" target="_blank">CVE-2020-3956</a> is a proof of concept exploit for a VMware Cloud Director remote code execution vulnerability. Full writeup <a href="https://citadelo.com/en/blog/full-infrastructure-takeover-of-vmware-cloud-director-CVE-2020-3956/" target="_blank">here</a>, demo <a href="https://youtu.be/TO40leo9y9w" target="_blank">here</a>.</li>
<li><a href="https://posts.specterops.io/covenant-v0-5-eee0507b85ba" target="_blank">Covenant v0.5</a> is not a new tool but this update includes a new cross platform .Net-Core implant: Brutes.</li>
<li><a href="https://labs.jumpsec.com/2020/06/03/shad0w/" target="_blank">shad0w</a> is a post exploitation framework designed to operate covertly on heavily monitored environments from <a href="https://twitter.com/_batsec_" target="_blank">@_batsec_</a> and is written in C, uses syscalls, blocks userland API hooking, and can load basically anything (.Net, DLL, EXE, VBS, JS, XSL) into memory. Code <a href="https://github.com/bats3c/shad0w" target="_blank">here</a>.</li>
<li><a href="https://github.com/TarlogicSecurity/kerbrute" target="_blank">kerbrute</a> is a script to perform kerberos bruteforcing by using impacket.</li>
<li><a href="https://github.com/N1ght-W0lf/HawkEye" target="_blank">HawkEye</a> is a malware dynamic instrumentation tool based on frida.re framework. It will hook common functions to log malware activities and output the results in a nice web page report. Use it in your sandbox to get nice HTML reports. Demo <a href="https://youtu.be/DnCj2Dt6OcE" target="_blank">here</a>.</li>
<li><a href="https://github.com/Flangvik/SharpCollection" target="_blank">SharpCollection</a> is a repository of nightly builds of common C# offensive tools, fresh from their respective master branches built and released in a CDI fashion using Azure DevOps release pipelines. Great use of CI to keep tools fresh and built for different framework versions.</li>
<li><a href="https://github.com/cedowens/SwiftBelt" target="_blank">SwiftBelt</a> is a macOS enumerator inspired by <a href="https://twitter.com/HarmJ0y" target="_blank">@harmj0y</a>'s Windows-based Seatbelt enumeration tool. SwiftBelt does not utilize any command line utilities and instead uses Swift code (leveraging the Cocoa Framework, Foundation libraries, OSAKit libraries, etc.) to perform system enumeration. This can be leveraged on the offensive side to perform enumeration once you gain access to a macOS host. I</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/Screetsec/Sudomy" target="_blank">Sudomy</a> is a subdomain enumeration tool, created using a bash script, to analyze domains and collect subdomains in fast and comprehensive way. This one is fairly new (30 days) so it must have slipped by, but looks to have very good results for a one shot subdomain enumeration tool. Give it a try on your next assessment or bug bounty.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
