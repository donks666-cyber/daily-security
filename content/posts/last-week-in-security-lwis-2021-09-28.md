Title: Last Week in Security (LWiS) - 2021-09-28
Date: 2021-09-28 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-09-28
Author: Erik
Summary: PPLDump BOF (<a href="https://twitter.com/the_bit_diddler" target="_blank">@the_bit_diddler</a>), code-signed rootkits (<a href="https://twitter.com/HackingThings" target="_blank">@HackingThings</a>), remote windows password resets (<a href="https://twitter.com/n00py1" target="_blank">@n00py1</a>), XSS to RCE (<a href="https://twitter.com/whynotsecurity" target="_blank">@whynotsecurity</a>), FinSpy bootkit (<a href="https://twitter.com/kaspersky" target="_blank">@kaspersky</a>), Azure brute-forceable endpoint (<a href="https://twitter.com/DrAzureAD" target="_blank">@DrAzureAD</a>?), and no C2 drama!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-09-20 to 2021-09-28.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://habr.com/en/post/579714/" target="_blank">Disclosure of three 0-day iOS vulnerabilities and critique of Apple Security Bounty program</a>. Criticism of Apple's bug bounty program has been growing, and it's pretty clear there is a problem. For a company with as much cash on hand as Apple (nearly 200 billion USD), the bad press from this can't be worth it, right? Another researched joined in the 0day releases with <a href="https://github.com/impost0r/Rotten-Apples/blob/main/README.md" target="_blank">Rotten-Apples</a>.</li>
<li><a href="https://www.offensive-security.com/exp312-osmr/" target="_blank">macOS Control Bypasses - New course for 2021</a>. It's great to see macOS get attention from training vendors. This course is only available in a subscription model which is an interesting pricing strategy from a vendor known for its relatively affordable a la cart training.</li>
<li><a href="https://blogs.vmware.com/teamfusion/2021/09/fusion-for-m1-public-tech-preview-now-available.html" target="_blank">Announcement: VMware Fusion for Apple silicon Public Tech Preview Now Available</a>. It only support Arm Linux virtual machines, no Arm Windows builds for now (as there is no way to legally license them for VM use).</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.google/threat-analysis-group/financially-motivated-actor-breaks-certificate-parsing-avoid-detection/" target="_blank">Financially motivated actor breaks certificate parsing to avoid detection</a>. By using End of Content markers in fixed length encoding, adware distributers were able to trick non-OpenSSL based products (i.e. Windows) to believe an invalid PE signature is actually valid. This is a neat trick, and I'm a bit surprised to see it burned on adware. Who else was aware/using it too?</li>
<li><a href="https://whynotsecurity.com/blog/xss-to-rce/" target="_blank">XSS to RCE: Covert Target Websites into Payload Landing Pages</a>. I really like this idea for delivering payloads for a red teaming phish, assuming the customer site is vulnerable to XSS that is otherwise not very valuable in terms of the assessment objectives.</li>
<li><a href="https://securitylab.github.com/research/in_the_wild_chrome_cve_2021_30632/" target="_blank">Chrome in-the-wild bug analysis: CVE-2021-30632</a>. Dig into the internals of the V8 JIT engine with GitHub as they analyzed this browser bug. PoC <a href="https://github.com/Lagal1990/CVE-2021-30632" target="_blank">here</a>.</li>
<li><a href="https://securitylab.github.com/research/apache-dubbo/" target="_blank">Apache Dubbo: All roads lead to RCE</a>. More GitHub technical content, this time a great article that goes from target identification to RCE using CodeQL. Be sure to check this out if you aren't using CodeQL for source code analysis/bug hunting.</li>
<li><a href="https://www.n00py.io/2021/09/resetting-expired-passwords-remotely/" target="_blank">Resetting Expired Passwords Remotely</a>. Some great techniques to get past expired or must-be-reset passwords found on a Windows network.</li>
<li><a href="https://labs.bishopfox.com/tech-blog/iam-vulnerable-assessing-the-aws-assessment-tools" target="_blank">IAM Vulnerable - Assessing the AWS Assessment Tools</a>. This is a great test of the four major open source AWS IAM misconfiguration assessment tools. I wonder if the IAM Vulnerable project could be used with CI/CD for these tools to show "live" coverage of the test cases as they improve.</li>
<li><a href="https://labs.bishopfox.com/tech-blog/an-intro-to-fuzzing-aka-fuzz-testing" target="_blank">An Intro to Fuzzing (AKA Fuzz Testing)</a>. Just what the title says. One of the best intro articles that covers the basics.</li>
<li><a href="https://theevilbit.github.io/beyond/beyond_0020/" target="_blank">Beyond the good ol' LaunchAgents - 20 - Terminal Preferences</a>. Wild that this series is already up to 20. This one would only work against technical targets, as they have to open the terminal application to run your persistence.</li>
<li><a href="https://trenchant.io/pwn2own-2021-parallels-desktop-guest-to-host-escape/" target="_blank">Pwn2Own 2021: Parallels Desktop Guest to Host Escape</a>. "Many evenings it is easier for me to read other people’s research, but I won’t find vulnerabilities reading blog posts. You find them by trying to do your own research." Damn, got me there. I've got some original research cooking (slow cooking, but still cooking).</li>
<li><a href="https://arstechnica.com/information-technology/2021/09/new-azure-active-directory-password-brute-forcing-flaw-has-no-fix/?comments=1" target="_blank">New Azure Active Directory password brute-forcing flaw has no fix</a>. The Azure Active Directory Seamless Single Sign-On has been good for user enumeration since <a href="https://o365blog.com/post/desktopsso/" target="_blank">2019</a> but this new discovery allows brute forcing (via a web endpoint, so it will be slow) without even logging anywhere. Wild. A successful login will generate a log, but you can spray all day without alerting any organization that users pass-through authentication.</li>
<li><a href="https://eclypsium.com/2021/09/20/everyone-gets-a-rootkit/" target="_blank">Everyone Gets a Rootkit</a>. On Windows since Windows 8 the Windows Platform Binary Table has a weakness that can allow an attacker to run malicious code with kernel privileges when a device boots up. WPBT is a feature that allows OEMs to modify the host operating system during boot to include vendor-specific drivers, applications, and content. Compromising this process can enable an attacker to install a rootkit compromising the integrity of the device.</li>
<li><a href="https://securelist.com/finspy-unseen-findings/104322/?utm_source=twitter&amp;utm_medium=social&amp;utm_campaign=gl_ESPO-SAS_je0066&amp;utm_content=link&amp;utm_term=gl_twitter_organic_366tqg9rxkpz34h" target="_blank">FinSpy: unseen findings</a>. What's better than a rootkit? A bootkit of course. FinSpy has been busy since it was last reported on in 2018 with some seriously advanced malware.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/boku7/injectEtwBypass" target="_blank">injectEtwBypass</a> is a  CobaltStrike BOF that injects an ETW bypass into a remote process via syscalls using HellsGate/HalosGate. This BOF contains some excellent assembly primitives for finding syscalls dynamically.</li>
<li><a href="https://github.com/EspressoCake/PPLDump_BOF" target="_blank">PPLDump_BOF</a> is a fully-fledged BOF to dump an arbitrary protected process.</li>
<li><a href="https://github.com/EspressoCake/Needle_Sift_BOF" target="_blank">Needle_Sift_BOF</a> is a file search bof to find strings within files without downloading the file from target. It uses <a href="https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strstr-wcsstr-mbsstr-mbsstr-l?view=msvc-160" target="_blank">strstr</a> to do the search, and is case sensitive (no strcasestr function in Windows).</li>
<li><a href="https://www.certego.net/en/news/dragonfly/" target="_blank">Dragonfly: your next generation malware sandbox</a>. A new sandbox with rules engine. Details are light but it looks like this sandbox uses binary emulation vs running samples in an instrumented virtual machine. Sign up for the Alpha <a href="https://dragonfly.certego.net/register" target="_blank">here</a>.</li>
<li><a href="https://github.com/mgeeky/ThreadStackSpoofer" target="_blank">ThreadStackSpoofer</a> is a PoC for an advanced In-Memory evasion technique allowing to better hide injected shellcode's memory allocation from scanners and analysts.</li>
<li><a href="https://github.com/ovotech/gitoops" target="_blank">gitoops</a> is Bloodhound for GitHub organizations by abusing CI/CD pipelines and GitHub access controls.</li>
<li><a href="https://github.com/waleedassar/SyscallNumberExtractor" target="_blank">SyscallNumberExtractor</a> exports all ntdll.dll syscalls to syscalls.txt. Useful for hard coding direct syscalls if not using a *gate technique.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
