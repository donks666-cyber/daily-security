Title: Last Week in Security (LWiS) - 2021-03-29
Date: 2021-03-29 23:32
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-03-29
Author: Erik
Summary: Real APT discovery (<a href="https://twitter.com/IgorBog61650384/" target="_blank">@IgorBog61650384</a>), a new heap exploitation technique (<a href="https://twitter.com/Dooflin5" target="_blank">@Dooflin5</a>), SAML injection (<a href="https://twitter.com/NCCGroupInfosec" target="_blank">@NCCGroupInfosec</a>), MemoryLoader IDA plugin (<a href="https://twitter.com/RRBlackRussian" target="_blank">@RRBlackRussian</a>), redacted PEM key recovery (<a href="https://twitter.com/cryptohack__" target="_blank">@CryptoHack__</a>), MirrorDump tool (<a href="https://twitter.com/_EthicalChaos_" target="_blank">@_EthicalChaos_</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-03-22 to 2021-03-29.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://www.microsoft.com/security/blog/2021/03/26/securing-our-approach-to-domain-fronting-within-azure/" target="_blank">Securing our approach to domain fronting within Azure</a>. The last of the major cloud services is killing domain fronting, thus further reducing the number of domains possible to front behind. <a href="https://fortynorthsecurity.com/blog/fastly-and-fronting/" target="_blank">Fastly</a> is about to see some new customers. With Encrypted Client Hello (ECH) on the horizon, there is hope for <a href="https://youtu.be/TDg092qe50g" target="_blank">a new kind of "fronting"</a>.</li>
<li><a href="https://news-web.php.net/php.internals/113838" target="_blank">Changes to Git commit workflow</a>. A tame title to an alarming update about an attacker with access to git.php.net that was committing <a href="https://github.com/php/php-src/commit/c730aa26bd52829a49f2ad284b181b7e82a68d7d" target="_blank">backdoors</a> to the php codebase. Good on php for catching this very quickly. How many projects has this happened to and no one has noticed? Does your app depend on those projects?</li>
<li><a href="https://www.microsoft.com/en-us/msrc/bounty-applications" target="_blank">Microsoft Applications Bounty Program</a>. Microsoft launches a new bounty program focused on apps. Perhaps in response to the <a href="https://github.com/oskarsve/ms-teams-rce/blob/main/README.md" target="_blank">"Important, Spoofing"</a> RCE in Teams from December 2020?</li>
<li><a href="https://www.vice.com/en/article/pkdjab/encrochat-signal-protocol-encryption" target="_blank">Encrypted Phone Firm Encrochat Used Signal Protocol</a>. The signal protocol remains unbroken, even by law enforcement. The end user devices however...</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://maxwelldulin.com/BlogPost?post=2257705984" target="_blank">House of Mind - Fastbin Variant in 2021</a>. This post (re)introduces GLibC heap exploitation method that works across all versions of the heap allocator and gives a write-what-where primitive. This is dense exploit development content.</li>
<li><a href="https://igor-blue.github.io/2021/03/24/apt1.html" target="_blank">APT Encounters of the Third Kind</a>. Easily the best article of the week. Igor goes from noticing a discrepancy between his test setup and production pcap time vs packet counts to uncovering an in-memory only APT backdoor. If you are wondering what a real advanced persistent threat looks like, this is it.</li>
<li><a href="https://research.nccgroup.com/2021/03/29/saml-xml-injection/" target="_blank">SAML XML Injection</a>. If you're testing an app with SSO abilities based on SAML, be sure to read this post.</li>
<li><a href="https://blog.palantir.com/phishcatch-detecting-password-reuse-from-the-inside-out-77aa93e3e6fb" target="_blank">PhishCatch: Detecting password reuse from the inside out</a>. By hashing enterprise passwords and storing them locally, and hashing all passwords to compare, this Chrome extension can detect password reuse without compromising any credentials.</li>
<li><a href="https://blog.cryptohack.org/twitter-secrets" target="_blank">Recovering a full PEM Private Key when half of it is redacted</a>. In just a few hours the wizards of the cryptohack Discord server managed to recover a RSA private key from a partially redacted screenshot. "Whether it’s a single bit leaking with Ladder Leak, or pieces of primes for a Coppersmith attack, partial information exposure of cryptographic private keys is often enough to totally break the crypto protocol. If you find something private, keep it that way."</li>
<li><a href="https://o365blog.com/post/mdm/" target="_blank">Bypassing conditional access by faking device compliance.</a>. This guide shows two different ways to make a device compliant in Microsoft InTune, even if you spoof it as a Commodore64.</li>
<li><a href="https://www.pentestpartners.com/security-blog/dumping-lsass-in-memory-undetected-using-mirrordump/" target="_blank">Dumping LSASS in memory undetected using MirrorDump</a>. Using <a href="https://github.com/boo-lang/boo" target="_blank">boo</a> and avoiding the classic dumping technique of calling OpenProcess, <a href="https://github.com/CCob/MirrorDump" target="_blank">MirrorDump</a> instead registers as a "legitimate" authentication provider with Windows and uses a handle to itself (lsass.exe) to do the dumping.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://labs.sentinelone.com/keep-malware-off-your-disk-with-sentinelones-ida-pro-memory-loader-plugin/" target="_blank">Keep Malware Off Your Disk With SentinelOne’s IDA Pro Memory Loader Plugin</a>. Download files straight from VirusTotal into memory and open in IDA Pro without writing them to disk. Neat!</li>
<li><a href="https://github.com/S4R1N/ZoomPersistence" target="_blank">ZoomPersistence</a> is an aggressor script and C++ shim to persist as Zoom on a Windows system by moving the user's zoom binary and replacing it with a shim.</li>
<li><a href="https://github.com/GONZOsint/gitrecon" target="_blank">gitrecon</a> is an OSINT tool to get information from a Github or Gitlab profile and find user's email addresses leaked on commits.</li>
<li><a href="https://github.com/hasherezade/malware_training_vol1" target="_blank">malware_training_vol1</a> is a work in progress repo of materials for Windows Malware Analysis training (volume 1).</li>
<li><a href="https://github.com/CyborgSecurity/PoisonApple" target="_blank">PoisonApple</a> is a command-line tool to perform various persistence mechanism techniques on macOS. It's missing a few from the new <a href="https://theevilbit.github.io/beyond/beyond_intro/" target="_blank">Beyond the good ol' LaunchAgents</a> series, but has others not covered there.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/trailofbits/graphtage" target="_blank">graphtage</a> is a command-line utility and underlying library for semantically comparing and merging tree-like structures, such as JSON, XML, HTML, YAML, plist, and CSS files. This is sure to be useful in a shell script at some point.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
