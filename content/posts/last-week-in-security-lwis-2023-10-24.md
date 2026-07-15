Title: Last Week in Security (LWiS) - 2023-10-24
Date: 2023-10-24 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2023-10-24
Author: Erik
Summary: Windows LPE (<a href="https://twitter.com/chompie1337" target="_blank">@chompie1337</a>), TPM Bitlocker deepdive (<a href="https://infosec.exchange/@itm4n" target="_blank">@itm4n@infosec.exchange</a>), unhooking effects (<a href="https://twitter.com/dazzyddos" target="_blank">@dazzyddos</a>), CastGuard (<a href="https://infosec.exchange/@gsuberland@chaos.social" target="_blank">@gsuberland@chaos.social</a>), Apple OTA -&gt; kernel hack (<a href="https://twitter.com/patch1t" target="_blank">@patch1t</a>), FalconHound (<a href="https://twitter.com/olafhartong" target="_blank">@olafhartong</a>), GraphRunner (<a href="https://twitter.com/dafthack" target="_blank">@dafthack</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2023-10-09 to 2023-10-23.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><p><a href="https://sec.okta.com/harfiles" target="_blank">Tracking Unauthorized Access to Okta's Support System</a>. Okta had another compromise.</p>
<blockquote>
<ul>
<li><a href="https://www.beyondtrust.com/blog/entry/okta-support-unit-breach" target="_blank">BeyondTrust Discovers Breach of Okta Support Unit</a>. Bad when your customers tell you that you're pwned.</li>
<li><a href="https://blog.cloudflare.com/how-cloudflare-mitigated-yet-another-okta-compromise/" target="_blank">How Cloudflare mitigated yet another Okta compromise</a>. Worse when its multiple customers.</li>
<li><a href="https://blog.1password.com/files/okta-incident/okta-incident-report.pdf" target="_blank">[PDF] Security Incident report [Internal Report]</a>. "[the suspected compromised endpoint] was scanned with the free version of Malwarebytes, which reported no findings." I'm not sure what I'm more concerned about: the IR process at 1Password is to run free AV against the endpoint or that the CTO happily published that fact.</li>
</ul>
</blockquote>
</li>
<li><p><a href="https://labs.watchtowr.com/curl-cve-2023-38545-its-still-not-the-end-of-the-world/" target="_blank">The Sky Has Not Yet Fallen - Curl (CVE-2023-38545)</a>. With the hype from the curl author himself ("Buckle up.") I was expecting more out of this bug. It's a pretty niche use case that is exploitable (client using a malicious proxy with curl). <a href="https://hackerone.com/reports/2187833" target="_blank">Here</a> is the hackerone report.</p>
</li>
<li><p><a href="https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z" target="_blank">Multiple Vulnerabilities in Cisco IOS XE Software Web UI Feature</a>. A CVSS 10.0 - yikes. Please stop putting admin interfaces for these critical network devices on the internet. I haven't found a legitimate public PoC yet (probably for the best).</p>
</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://securityintelligence.com/x-force/critically-close-to-zero-day-exploiting-microsoft-kernel-streaming-service/" target="_blank">Critically close to zero(day): Exploiting Microsoft Kernel streaming service</a>. A nice new attack surface in Window. PoC <a href="https://github.com/xforcered/Windows_MSKSSRV_LPE_CVE-2023-36802" target="_blank">here</a>.</li>
<li><a href="https://rhinosecuritylabs.com/aws/attacking-aws-cognito-with-pacu-p1/" target="_blank">Attacking AWS Cognito with Pacu</a> . Don't miss <a href="https://rhinosecuritylabs.com/aws/attacking-aws-cognito-with-pacu-p2/" target="_blank">part 2</a>. More good cloud assessment content from Rhino security labs.</li>
<li><a href="https://googleprojectzero.blogspot.com/2023/10/an-analysis-of-an-in-the-wild-ios-safari-sandbox-escape.html" target="_blank">An analysis of an in-the-wild iOS Safari WebContent to GPU Process exploit</a>. Some very hardcore analysis of a complicated bug chain with a simple buffer overflow to kick it off - with a nice bit of shade toward Apple in the conclusion.</li>
<li><a href="https://itm4n.github.io/tpm-based-bitlocker/" target="_blank">A Deep Dive into TPM-based BitLocker Drive Encryption</a>. I always love an itm4n post - the right amount of depth and screenshots.</li>
<li><a href="https://www.shielder.com/blog/2023/10/cve-2023-33466-exploiting-healthcare-servers-with-polyglot-files/" target="_blank">CVE-2023-33466 - Exploiting Healthcare Servers with Polyglot Files</a>. A good real-world example of a polygot file exploit.</li>
<li><a href="https://dazzyddos.github.io/posts/(Un)Hooking,-COWs-and-Meow-Meow/" target="_blank">(Un)Hooking, COWs and Meow Meow</a>. When you modify ntdll in memory (i.e. hooking/unhooking), you really load a second copy into your process memory space.</li>
<li><a href="https://dirkjanm.io/phishing-for-microsoft-entra-primary-refresh-tokens/" target="_blank">Phishing for Primary Refresh Tokens and Windows Hello keys</a>. A nice method to go from device code phish to persistent in Entra ID. Check the <a href="https://github.com/kiwids0220/deviceCode2WinHello" target="_blank">deviceCode2WinHello</a> script as well.</li>
<li><a href="https://labs.nettitude.com/blog/preventing-type-confusion-with-castguard/" target="_blank">Preventing Type Confusion with CastGuard</a>. A new yet-undocumented Windows exploit mitigation feature is coming.</li>
<li><a href="https://jhftss.github.io/The-Nightmare-of-Apple-OTA-Update/" target="_blank">The Nightmare of Apple's OTA Update: Bypassing the Signature Verification and Pwning the Kernel</a>. A nice bug chain that led to kernel compromise (even with SIP enabled). Great work.</li>
<li><a href="https://labs.watchtowr.com/ghost-in-the-wire-sonic-in-the-wall/" target="_blank">Ghost In The Wire, Sonic In The Wall - Adventures With SonicWall</a>. End result is a few DoS bugs, but the process is nicely documented.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/evilsocket/legba" target="_blank">legba</a> - A multiprotocol credentials bruteforcer / password sprayer and enumerator.</li>
<li><a href="https://github.com/Cr4sh/pico_dma" target="_blank">pico_dma</a> - Autonomous pre-boot DMA attack hardware implant for M.2 slot based on PicoEVB development board.</li>
<li><a href="https://github.com/hfiref0x/KDU/releases/tag/v1.4.0" target="_blank">Kernel Driver Utility v1.4.0</a> - 4 new providers and a dump command!</li>
<li><a href="https://github.com/kleiton0x00/Proxy-DLL-Loads" target="_blank">Proxy-DLL-Loads</a> - A proof of concept demonstrating the DLL-load proxying using undocumented Syscalls.</li>
<li><a href="https://github.com/RtlDallas/Jomungand" target="_blank">Jomungand</a> - Shellcode Loader with memory evasion.</li>
<li><a href="https://github.com/BlackSnufkin/NovaLdr" target="_blank">NovaLdr</a> - Threadless Module Stomping In Rust with some features.</li>
<li><a href="https://github.com/RoseSecurity-Research/WolfPack" target="_blank">WolfPack</a> - WolfPack combines the capabilities of Terraform and Packer to streamline the deployment of red team redirectors on a large scale.</li>
<li><a href="https://github.com/FalconForceTeam/FalconHound" target="_blank">FalconHound</a> - FalconHound is a blue team multi-tool. It allows you to utilize and enhance the power of BloodHound in a more automated fashion. It is designed to be used in conjunction with a SIEM or other log aggregation tool.</li>
<li><a href="https://github.com/dafthack/GraphRunner" target="_blank">GraphRunner</a> - A Post-exploitation Toolset for Interacting with the Microsoft Graph API.</li>
<li><a href="https://github.com/cjm00n/EvilSln" target="_blank">EvilSln</a> - A New Exploitation Technique for Visual Studio Projects.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/anrbn/GATOR" target="_blank">GATOR</a> - GCP Attack Toolkit for Offensive Research, a tool designed to aid in research and exploiting Google Cloud Environments.</li>
<li><a href="https://github.com/Wh04m1001/CVE-2023-36723" target="_blank">CVE-2023-36723</a> - PoC for arbitrary directory creation bug in Windows Container Manager service.</li>
<li><a href="https://github.com/tinyproxy/tinyproxy" target="_blank">tinyproxy</a> - a light-weight HTTP/HTTPS proxy daemon for POSIX operating systems.</li>
<li><a href="https://github.com/TalAloni/SMBLibrary" target="_blank">SMBLibrary</a> - Free, Open Source, User-Mode SMB 1.0/CIFS, SMB 2.0, SMB 2.1 and SMB 3.0 server and client library.</li>
<li><a href="https://github.com/souzomain/Shaco" target="_blank">Shaco</a> - Shaco is a linux agent for havoc.</li>
<li><a href="https://github.com/KCarretto/realm" target="_blank">realm</a> - Realm is a cross platform Red Team engagement platform with a focus on automation and reliability.</li>
<li><a href="https://github.com/Prepouce/CoercedPotato" target="_blank">CoercedPotato</a> - From Patate (LOCAL/NETWORK SERVICE) to SYSTEM by abusing SeImpersonatePrivilege on Windows 10, Windows 11 and Server 2022.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 425 (+0)</p>
<p>Blogs monitored: 358 (+0)</p>
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
