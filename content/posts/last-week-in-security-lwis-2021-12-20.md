Title: Last Week in Security (LWiS) - 2021-12-20
Date: 2021-12-20 22:25
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-12-20
Author: Erik
Summary: Explaining the 0click iOS exploit (<a href="https://twitter.com/i41nbeer" target="_blank">@i41nbeer</a> and <a href="https://twitter.com/5aelo" target="_blank">@5aelo</a>), new loader (<a href="https://twitter.com/zux0x3a" target="_blank">@zux0x3a</a>), first look at Nighthawk C2 (<a href="https://twitter.com/peterwintrsmith" target="_blank">@peterwintrsmith</a> and <a href="https://twitter.com/modexpblog" target="_blank">@modexpblog</a>), new injection technique (<a href="https://twitter.com/netero_1010" target="_blank">@netero_1010</a>), OST documentation (<a href="https://twitter.com/_nwodtuhs" target="_blank">@_nwodtuhs</a>), and more!

<aside class="m-note m-warning">
<h3>Holiday Break</h3>
<p>Last Week in Security will be taking two weeks off for the holidays. See you all next year!</p>
</aside>
<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-12-14 to 2021-12-20.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.praetorian.com/blog/log4j-2-15-0-stills-allows-for-exfiltration-of-sensitive-data/" target="_blank">Log4j 2.15.0 stills allows for exfiltration of sensitive data</a>. You'll be writing this one up on assessments for years to come. 2.16 was released but also had a <a href="https://issues.apache.org/jira/browse/LOG4J2-3230" target="_blank">DoS-able vulnerability</a>. Third patch is the charm? This whole saga has become the best example of <a href="https://xkcd.com/2347/" target="_blank">Dependency</a> in recent memory. If you need to exploit Log4j, grab the <a href="https://github.com/pimps/JNDI-Exploit-Kit/" target="_blank">JNDI-Exploit-Kit</a>. Trying to keep it all straight? This <a href="https://github.com/DickReverse/InfosecMindmaps/blob/main/Log4shell/AmIVulnerable-Log4shell-v6.1.png" target="_blank">flow chart</a> was up to date when published.</li>
<li><a href="https://securitylab.github.com/research/new-bug-slayer/" target="_blank">Updates to the Bug Slayer bug bounty program</a>. If you use <a href="https://codeql.github.com/" target="_blank">CodeQL</a> to find and report bugs, you may be eligible for a bonus bounty.</li>
<li><a href="https://www.mdsec.co.uk/2021/12/nighthawk-0-1-new-beginnings/" target="_blank">Nighthawk 0.1 – New Beginnings</a>. MDSec releases more details about its impressive in-house C2 framework. I'd love to get my hands on it and test it out. DM's open ;).</li>
<li><a href="https://blog.tetrane.com/2021/REVEN-Free-Edition-VM.html" target="_blank">REVEN Free Edition - Available as a VM</a>. REVEN is a "Timeless Analysis" system that allows you to triage crashes more effectively. Now it's even easier to try out with a ready made virtual machine.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://labs.detectify.com/2021/12/15/zero-day-path-traversal-grafana/" target="_blank">How I found the Grafana zero-day Path Traversal exploit that gave me access to your logs</a>. A manual source code audit and some fuzzing found this arbitrary file read bug.</li>
<li><a href="https://googleprojectzero.blogspot.com/2021/12/a-deep-dive-into-nso-zero-click.html" target="_blank">A deep dive into an NSO zero-click iMessage exploit: Remote Code Execution</a>. Wow. NSO used a JBIG2 vulnerability to construct a custom computer architecture they then used to search and modify memory to carry out the next stage of the exploit chain. Talk about <a href="https://en.wikipedia.org/wiki/Weird_machine" target="_blank">weird machines</a>.</li>
<li><a href="https://0xsp.com/security%20research%20&amp;%20development%20(SRD)/defeat-the-castle-bypass-av-advanced-xdr-solutions" target="_blank">Defeat the Castle - Bypass AV &amp; Advanced XDR solutions.</a>. AV/EDR solutions seem to struggle with the double encryption/encoding used here. Tool available <a href="https://github.com/0xsp-SRD/mortar" target="_blank">here</a>.</li>
<li><a href="https://palant.info/2021/12/20/yes-fun-browser-extensions-can-have-vulnerabilities-too/" target="_blank">Yes, fun browser extensions can have vulnerabilities too!</a>. "A one-time visit to a malicious website would have been sufficient to compromise the browser integrity permanently." It's time to start thinking of browsers as OSs and extensions as programs running as root.</li>
<li><a href="https://www.netero1010-securitylab.com/eavsion/alternative-process-injection" target="_blank">Alternative Process Injection</a>. This processes injects shellcode into the already loaded DLL memory page, which gets around most (but not all) indicators of injection.</li>
<li><a href="https://hello.fieldeffect.com/hubfs/Blackswan/Blackswan_Technical_Write%20Up_Field_Effect.pdf" target="_blank">Blackswan Technical Writeup (PDF)</a>. Six Windows privescs with beautifully presented write ups? Yes please.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><dl>
<dt>Cobalt Strike 4.5 Update Specifics:</dt>
<dd><ul>
<li><a href="https://www.cobaltstrike.com/blog/writing-beacon-object-files-flexible-stealthy-and-compatible/" target="_blank">Writing Beacon Object Files: Flexible, Stealthy, and Compatible</a>. This post is great as it covers lesser used concepts like syscalls in x86 BOFs.</li>
<li><a href="https://www.cobaltstrike.com/blog/process-injection-update-in-cobalt-strike-4-5/" target="_blank">Process Injection Update in Cobalt Strike 4.5</a></li>
<li><a href="https://www.cobaltstrike.com/blog/user-defined-reflective-loader-udrl-update-in-cobalt-strike-4-5/" target="_blank">User Defined Reflective Loader (UDRL) Update in Cobalt Strike 4.5</a></li>
<li><a href="https://www.cobaltstrike.com/blog/sleep-mask-update-in-cobalt-strike-4-5/" target="_blank">Sleep Mask Update in Cobalt Strike 4.5</a></li>
<li><a href="https://www.cobaltstrike.com/blog/a-deeper-look-into-the-max-retry-strategy-option/" target="_blank">A Deeper Look Into the Max Retry Strategy Option</a></li>
</ul>
</dd>
</dl>
</li>
<li><a href="https://github.com/mufeedvh/moonwalk" target="_blank">moonwalk</a> helps cover your tracks during Linux Exploitation by leaving zero traces on system logs and filesystem timestamps.</li>
<li><a href="https://tools.thehacker.recipes/" target="_blank">The Hacker Tools</a> is focused on documenting and giving tips &amp; tricks on common infosec tools. This is an awesome initiative and an idea I've had for a while. Happy to see it being executed.</li>
<li><a href="https://github.com/DallasFR/Cobalt-Clip" target="_blank">Cobalt-Clip</a> is clipboard addons for Cobalt Strike to interact with clipboard. With this you can dump, edit and monitor the content of a clipboard.</li>
<li><a href="https://github.com/vfsfitvnm/intruducer" target="_blank">intruducer</a> is a Rust crate to load a linux shared library into a target process without using ptrace.</li>
<li><a href="https://github.com/VollRagm/KernelSharp" target="_blank">KernelSharp</a>  is an example of how to use NativeAOT to compile C# code to a Windows Kernel Mode driver.</li>
<li><a href="https://github.com/VollRagm/KernelBypassSharp" target="_blank">KernelBypassSharp</a> is a C# Kernel Mode Driver to read and write memory in protected processes.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/FSecureLABS/awspx" target="_blank">awspx</a> is a graph-based tool for visualizing effective access and resource relationships in AWS environments.</li>
<li><a href="https://github.com/facebook/mariana-trench" target="_blank">mariana-trench</a> is Facebook's security focused static analysis tool for Android and Java applications.</li>
<li><a href="https://github.com/61106960/adPEAS" target="_blank">adPEAS</a>. Note this is not part of the "official" PEAS toolset. It's a  Powershell tool to automate Active Directory enumeration.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
