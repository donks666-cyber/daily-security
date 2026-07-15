Title: Last Week in Security (LWiS) - 2020-09-21
Date: 2020-09-21 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2020-09-21
Author: Erik
Summary: Argument injection makes a comeback by <a href="https://twitter.com/dozernz" target="_blank">@dozernz</a>, persistence with the Dock in macOS by <a href="https://twitter.com/_D00mfist" target="_blank">@_D00mfist</a>, the nuclear option for unhooking by <a href="https://twitter.com/winternl_t" target="_blank">@winternl_t</a>, DCOM lateral movement by <a href="https://twitter.com/domchell" target="_blank">@domchell</a>, a better MitM by <a href="https://twitter.com/httptoolkit" target="_blank">@HttpToolkit</a>, owning Firefox on Android by <a href="https://twitter.com/LukasStefanko" target="_blank">@LukasStefanko</a>, and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2020-09-14 to 2020-09-21.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.zdnet.com/article/first-death-reported-following-a-ransomware-attack-on-a-german-hospital/" target="_blank">First death reported following a ransomware attack on a hospital</a>. A patient that had to be diverted due to ransomware affecting a hospital in Germany dies. The cyber and physical world are merging, with all the good and bad that brings.</li>
<li><a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon" target="_blank">Sysmon v12.0</a> was released which includes the ability to do clipboard monitoring. Be aware that this <a href="https://twitter.com/Cyb3rWard0g/status/1306795536322879489" target="_blank">will store passwords</a> or other secrets that make it into the clipboard.</li>
<li><a href="https://www.justice.gov/opa/pr/two-iranian-nationals-charged-cyber-theft-campaign-targeting-computer-systems-united-states" target="_blank">Two Iranian Nationals Charged in Cyber Theft Campaign Targeting Computer Systems in United States, Europe, and the Middle East</a>. Part of the US strategy against foreign hackers has been to call them out and charge individual operators. In this case it is two Iranians who have operated since at least 2013 and attacked civilian, industry, and government targets.</li>
<li><a href="https://www.zdnet.com/google-amp/article/us-charges-five-hackers-part-of-chinese-state-sponsored-group-apt41/" target="_blank">US charges five hackers from Chinese state-sponsored group APT41</a>. The name-and-shame campaign continues, this time targeting the Chinese APT 41. It's important to note that these are charges for hacking private companies for non-intelligence related reasons (i.e. intellectual property theft), as the US likely doesn't want to make "legitimate" spying illegal.</li>
<li><a href="https://github.blog/2020-09-17-github-cli-1-0-is-now-available/" target="_blank">GitHub CLI 1.0 is now available</a>. GitHub rolls out a cross-platform command line tool written in Go. Now you can perform all your GitHub actions without having to leave the terminal. This was true before using raw git, but now you can do things like manage merge requests, issues, and more from the command line.</li>
<li><a href="https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf" target="_blank">The art and science of detecting Cobalt Strike</a>. Cisco Talos researches spent some time getting very familiar with Cobalt Strike and produced more than 50 new snort and ClamAV signatures. Read this and get to work in Artifact Kit to ensure these rules won't catch you.</li>
<li><a href="https://github.com/Ne0nd0g/merlin/releases/tag/v0.9.0-beta" target="_blank">merlin 0.9.0 release</a> adds new features and agent types, but my favorite addition has to be the live JA3 signature modification capability for agents. Very cool!</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://dozer.nz/posts/aruba-clearpass-rce" target="_blank">Aruba Clearpass RCE (CVE-2020-7115)</a>. Argument injection is an under appreciated bug class, but it is more powerful and more widespread than most researchers realize. In this case Daniel uses some nifty tricks to get a root reverse shell.</li>
<li><a href="https://s3cur3th1ssh1t.github.io/Building-a-custom-Mimikatz-binary/" target="_blank">Building a custom Mimikatz binary</a> shows how red teamers can take open source tools, and modify the source code to bypass most static detections. You'll have to do some more work for advanced EDR detections based on dynamic or behavioral analysis.</li>
<li><a href="https://posts.specterops.io/are-you-docking-kidding-me-9aa79c24bdc1" target="_blank">Are You Docking Kidding Me?</a>. In this post, Leo Pitt shows the macOS equivalent of using LNK files on Windows to persist in the Dock on macOS. The post ends with a very thorough detection section.</li>
<li><a href="https://blog.cobaltstrike.com/2020/09/17/beacon-object-file-adventures-some-zerologon-smbghost-and-situational-awareness/" target="_blank">Beacon Object File ADVENTURES: Some Zerologon, SMBGhost, and Situational Awareness</a>. Beacon object files (BOFs) are a new capability in Cobalt Strike that allow for compiled code to run in the context of a beacon. This post introduces two exploits and a bunch of situational awareness BOFs to get you started.</li>
<li><a href="https://teamhydra.blog/2020/09/18/implementing-direct-syscalls-using-hells-gate/">Implementing Direct Syscalls Using Hell’s Gate</a>. Instead of baking your syscall numbers into your binary (and having to keep a list of them for every OS), use the Hell's Gate technique (<a href="https://blog.badsectorlabs.com/last-week-in-security-lwis-2020-06-08.html">LWiS 2020-06-08</a>) to determine them dynamically. PoC <a href="https://github.com/N4kedTurtle/HellsGatePoC">here</a>.</li>
<li><a href="https://www.trustedsec.com/blog/macos-injection-via-third-party-frameworks/" target="_blank">MacOS Injection via Third-Party Frameworks</a>. This is some great macOS research by Adam Chester that shows how apps that use debugging pipes (like Fiddler or VSCode) for injection as well as Electron apps for Transparency, Consent, and Control (TCC) bypass/obfuscation.</li>
<li><a href="https://winternl.com/memfuck/" target="_blank">MemFuck: Bypassing User-Mode Hooks</a>. Sometimes you want to remove ALL the usermode hooks from your process by unmapping everything you can. In that case this project is for you - it uses some really interesting tricks to unmap DLLs and then use direct syscalls. PoC <a href="https://github.com/jackullrich/memfuck" target="_blank">here</a>.</li>
<li><a href="https://www.mdsec.co.uk/2020/09/i-like-to-move-it-windows-lateral-movement-part-2-dcom/" target="_blank">I Like to Move It: Windows Lateral Movement Part 2 – DCOM</a>. Dominic Chell shows how DCOM can be used for lateral movement in a Windows network, including using Excel 4 macros for lateral movement.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/Mr-Un1k0d3r/DLLsForHackers" target="_blank">DLLsForHackers</a> generates Dlls that can be used for side loading and other attack vectors. This Dll will (maybe) not cause deadlock since it only use functions that are DllMain safe (unlike many other tools/DLL hijacking techniques). For a potentially more mature tool, see <a href="https://github.com/monoxgas/Koppeling" target="_blank">Koppeling</a>.</li>
<li><a href="https://github.com/sdushantha/tmpmail" target="_blank">tmpmail</a> is a command line utility that allows you to create a temporary email address and receive emails to the temporary email address. It uses <a href="https://www.1secmail.com/api/" target="_blank">1secmail's API</a> to receive emails. Prefer python? <a href="https://github.com/aakash30jan/pydispo" target="_blank">pydispo</a> has you covered.</li>
<li><a href="https://github.com/Flangvik/AMSI.fail" target="_blank">AMSI.fail</a> is a C# Azure Function with an HTTP trigger that generates obfuscated PowerShell snippets that break or disable AMSI for the current process. Check out the live site: <a href="https://www.amsi.fail/" target="_blank">www.amsi.fail</a>.</li>
<li><a href="https://github.com/checkymander/sshiva" target="_blank">sshiva</a> is a C# application that allows you to run SSH commands against a host or list of hosts.</li>
<li><a href="https://github.com/FuzzySecurity/Sharp-Suite#discerningfinch" target="_blank">DiscerningFinch</a> collects an array of OS specific string constants and then attempts to use those to brute-force decrypt the inner binary. If it succeeds it loads the inner binary into memory passing along any command line arguments that may exists. If it fails, it prints out a .NET-looking error message as feedback.</li>
<li><a href="https://gitlab.com/gitlab-com/gl-security/security-operations/gl-redteam/red-team-tech-notes/-/tree/master/firefox-android-2020" target="_blank">Firefox for Android LAN-Based Intent Triggering</a>. The SSDP engine in Firefox for Android (68.11.0 and below) can be tricked into triggering Android intent URIs with zero user interaction. This attack can be leveraged by attackers on the same WiFi network and manifests as applications on the target device suddenly launching, without the users' permission, and conducting activities allowed by the intent. Demo <a href="https://gitlab.com/gitlab-com/gl-security/security-operations/gl-redteam/red-team-tech-notes/-/raw/master/firefox-android-2020/poc2.mp4" target="_blank">here</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/httptoolkit" target="_blank">HTTP Toolkit</a> is a cross platform, open source, HTTP MitM proxy. This looks super powerful, and easy to use. For HTTP request monitoring and modification, this looks easier to use than Burp Suite.</li>
<li><a href="https://github.com/mez-0/MoveScheduler" target="_blank">MoveScheduler</a> focuses on lateral movement via several different methods of scheduling tasks: Win32_ScheduledJob (C#), Win32_Scheduledjob (PowerShell), TaskScheduler Library, and PS_ScheduleTask.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/blog" target="_blank">SIXGEN's blog</a>.</p>
</section>
