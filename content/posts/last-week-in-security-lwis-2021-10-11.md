Title: Last Week in Security (LWiS) - 2021-10-11
Date: 2021-10-11 22:26
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-10-11
Author: Erik
Summary: iOS 15 IOMFB exploit (<a href="https://twitter.com/amarsaar" target="_blank">@AmarSaar</a>), new lsass dumper (<a href="https://twitter.com/thefLinkk" target="_blank">@thefLinkk</a>), SharpCalendar (<a href="https://twitter.com/sadpanda_sec" target="_blank">@sadpanda_sec</a>), gcpHound (<a href="https://twitter.com/desi_jarvis" target="_blank">@desi_jarvis</a> + <a href="https://twitter.com/Richarjb" target="_blank">@Richarjb</a>), macOS SBX (<a href="https://twitter.com/epsilan" target="_blank">@epsilan</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-10-06 to 2021-10-11.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://blogs.windows.com/windowsexperience/2021/08/31/windows-11-available-on-october-5/" target="_blank">Windows 11 available on October 5</a>. I suppose it's better than having another cryptic Windows 10 version? The difference between 1507 and 21H1 is pretty big and lots of people are on "Windows 10" versions that are not being updated without realizing it.</li>
<li><a href="https://techcrunch.com/2021/10/06/european-parliament-backs-ban-on-remote-biometric-surveillance/" target="_blank">European Parliament backs ban on remote biometric surveillance</a>. Not law yet, but a move in the right direction.</li>
<li><a href="https://www.trailofbits.com/post/announcing-osquery-5-now-with-endpointsecurity-on-macos" target="_blank">Announcing osquery 5: Now with EndpointSecurity on macOS</a>. The amazing osquery tool has been updated to use the latest Endpoint Security framework/API that Apple has been pushing recently after depreciating kernel extensions.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://bohops.com/2021/10/08/analyzing-and-detecting-a-vmtools-persistence-technique/" target="_blank">Analyzing and Detecting a VMTools Persistence Technique</a>. VMware tools binaries/services are commonly found on VMs and can be leveraged for persistence on power state changes. Unsure of how useful this would be in practice, as most legitimate target VMs would be in a datacenter somewhere powered on all the time?</li>
<li><a href="https://saaramar.github.io/IOMFB_integer_overflow_poc/" target="_blank">Bindiff and POC for the IOMFB vulnerability, iOS 15.0.2</a>. An "in the wild" exploit of IOMobileFrameBuffer is cited in the iOS 15.0.2 patch notes, and this bindiff and PoC is incredibly quick. In the end a reliable crash with arbitrary data is achieved. Update those iOS devices (and/or save your SHSH2 blobs ;). What's amazing is this analysis/PoC was completed and published in under 2 hours of the patch being released. Very impressive.</li>
<li><a href="https://desi-jarvis.medium.com/gcphound-a-swiss-army-knife-offensive-toolkit-for-google-cloud-platform-gcp-fb9e18b959b4" target="_blank">gcpHound: A Swiss Army Knife Offensive Toolkit for Google Cloud Platform (GCP)</a>. This is a perfect tool to run after you land on a developer's machine with <a href="https://desi-jarvis.medium.com/compromised-endpoint-to-compromised-gcp-gone-in-60-seconds-3229cc185863" target="_blank">GCP credentials</a>. Currently only available in the docker image <cite>desijarvis/gcphound:v1.1-beta</cite> and the tool is written in python at /root/gcpHound.</li>
<li><a href="https://github.com/ronwai/talks/blob/main/ObjectiveByTheSeaV4_EnvironmentalDisaster.pdf" target="_blank">Environmental Disaster - a LaunchServices Tale</a>. The ability to control environment variables when launching a process from an app sandbox on macOS leads to a few different kinds of sandbox escapes, with more likely lurking thanks to popular applications/frameworks and their use of environment variables that are not block-listed by Apple.</li>
<li><a href="https://rastamouse.me/backdoor-net-assemblies-with-dnspy-%f0%9f%a4%94/" target="_blank">Backdoor .NET assemblies with… dnSpy 🤔</a>. Everyone loves a good backdoor for persistence, data exfiltration, or even privilege escalation. .NET assesmblies can be modified to run arbitrary code with <a href="https://github.com/dnSpy/dnSpy" target="_blank">dnSpy</a>, and if exposed to the internet, could even be triggerable!</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/codewhitesec/HandleKatz" target="_blank">HandleKatz</a> is a position independent Lsass dumper abusing cloned handles, direct system calls and a modified version of minidumpwritedump(). The tool does not allocate any more executable memory and can therefore efficiently be combined with concepts such as <a href="https://www.forrest-orr.net/post/malicious-memory-artifacts-part-i-dll-hollowing" target="_blank">(Phantom)DLL-Hollowing</a> (unlike Donut, sRDI, etc).</li>
<li><a href="https://github.com/OG-Sadpanda/SharpCalendar" target="_blank">SharpCalendar</a> is a tool that uses Microsoft.Office.Interop.Excel to retrieve Outlook Calendar details in operator defined one month chunks. Sometimes its nice to know if/when someone will be out of office!</li>
<li><a href="https://github.com/boku7/Ninja_UUID_Dropper" target="_blank">Ninja_UUID_Dropper</a> is a loader that uses module stomping, no new thread, HellsGate syscaller, and UUID encoding for x64 Windows 10. The technique of encoding shellcode in UUIDs was first seen in <a href="https://research.nccgroup.com/2021/01/23/rift-analysing-a-lazarus-shellcode-execution-method/" target="_blank">Lazarus</a> malware.</li>
<li><a href="https://github.com/ricardojoserf/covert-tube" target="_blank">covert-tube</a> is a program to control systems remotely by uploading videos to Youtube using Python to create the videos and the listener. It creates videos with frames formed of simple text, QR codes with cleartext, or QR codes using AES encryption. It may be easier to use youtube comments/video descriptions with encrypted text instead of reading data out of the videos themselves?</li>
<li><a href="https://weakpass.com/wordlist/1948" target="_blank">weakpass_3a</a> is the latest weakpass wordlist. 107.77 GB of plaintext password goodness to feed your GPU cluster.</li>
<li><a href="https://github.com/MythicAgents/hermes" target="_blank">hermes</a> is a Swift 5 Mythic payload for macOS. It currently supports Mythic 2.2.8 and will update as necessary.</li>
<li><a href="https://github.com/plackyhacker/SuspendedThreadInjection" target="_blank">SuspendedThreadInjection</a> is a meterpreter injection technique using C# that attempts to bypass Defender.</li>
<li><a href="https://github.com/Kudaes/DInvoke_rs" target="_blank">DInvoke_rs</a> brings the popular DInvoke/direct syscall technique to Rust! I'm excited to see more rust tooling for red teams.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/FunnyWolf/Viper" target="_blank">Viper</a> is a graphical penetration tool that wraps metasploit in a nice, multi-user web-gui.</li>
<li><a href="https://github.com/Dreamacro/clash" target="_blank">Clash</a> is a rule-based tunnel daemon in Go that supports many protocols like VMess, Shadowsocks, Trojan, etc.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
