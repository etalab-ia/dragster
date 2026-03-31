# Changelog

## [0.2.0](https://github.com/etalab-ia/dragster/compare/v0.1.1...v0.2.0) (2026-03-31)


### Features

* add hooks, enable/disable, and ctx config for memory skill ([28a73c5](https://github.com/etalab-ia/dragster/commit/28a73c511ba5520060f31d7032f560b112e3833b))
* add memory skill for document ingestion tracking ([edeb898](https://github.com/etalab-ia/dragster/commit/edeb898e78d287aaa67695b006c81d9957836c16))
* add memory skill for document ingestion tracking ([ed5f6c8](https://github.com/etalab-ia/dragster/commit/ed5f6c8a36898939584041560e219d3ec59c5681))
* reorganize skills with provider metadata ([db18c2b](https://github.com/etalab-ia/dragster/commit/db18c2be57ddfc6c35195eee2273de07620e277d))
* reorganize skills with provider metadata ([549e04b](https://github.com/etalab-ia/dragster/commit/549e04bea5f52170ec1f91c19ab7db43856f86d6))


### Bug Fixes

* **ci:** update symlink validation for new .skills structure ([38dc879](https://github.com/etalab-ia/dragster/commit/38dc879f9f55337ba82241b7004cf9c5d2418b82))
* move skills to top-level directories ([880ed86](https://github.com/etalab-ia/dragster/commit/880ed86fffc258d9b8708d0c28db8d36ad8db5bb))
* update worktrunk hook name (post-create → pre-start) ([8d6a953](https://github.com/etalab-ia/dragster/commit/8d6a953ee3e5fedd40ee39ecefbf1914da7fd466))
* use individual skill symlinks instead of whole-directory symlink ([4cdb5a9](https://github.com/etalab-ia/dragster/commit/4cdb5a975ee4fb0d38995e6716676d52d3fb6e50))
* use individual skill symlinks instead of whole-directory symlink ([f454f37](https://github.com/etalab-ia/dragster/commit/f454f3797884caa9224dd0bab7a415b848c40b42))

## [0.1.1](https://github.com/etalab-ia/dragster/compare/v0.1.0...v0.1.1) (2026-03-25)


### Bug Fixes

* **ci:** add --no-project to uv run commands ([442af86](https://github.com/etalab-ia/dragster/commit/442af8654a757cf797b585caf4594168fb9ab4fe))
* **ci:** disable integration-letta-evals job entirely ([8259bc4](https://github.com/etalab-ia/dragster/commit/8259bc4e1d12cb224360614e1cb6aa74959c99ae))
* **ci:** move secrets check to step level ([2e41435](https://github.com/etalab-ia/dragster/commit/2e41435c0e8030b76728d002148e9f5a82bdbb38))
* **ci:** move secrets check to step level ([3941f56](https://github.com/etalab-ia/dragster/commit/3941f56a0baf7592cdadbb6cb128d9ebc8fe0865))
* **ci:** pass secrets via env and skip project install ([bc14e48](https://github.com/etalab-ia/dragster/commit/bc14e480951637c80b500c0295197e624f901386))
* **ci:** remove manual test script, mark integration job non-blocking ([1270a70](https://github.com/etalab-ia/dragster/commit/1270a704b468e9f2c11a2798da4bc5959f65b8b0))
* **deps:** install letta-evals from GitHub to get v0.11.0 ([390b60d](https://github.com/etalab-ia/dragster/commit/390b60de1e4f6f63e6bb11de4448c5f32d621caf))
* **deps:** install letta-evals from GitHub to get v0.11.0 ([3fced03](https://github.com/etalab-ia/dragster/commit/3fced03859600730e88d85489c5b4e4c1454d7a2))
* **evals:** remove response_quality grader (requires OpenAI key) ([014de29](https://github.com/etalab-ia/dragster/commit/014de295288dbbc82148398806d9822e50b61376))
* **evals:** update suite.yaml to match letta-evals 0.9.0 schema ([fef2c35](https://github.com/etalab-ia/dragster/commit/fef2c352839b3a4c29982bc6a8141574c3cc737a))
* **tests:** reduce setup-knowledge-base keywords to search+index ([cabd6ed](https://github.com/etalab-ia/dragster/commit/cabd6ed4f25c146957a78f54cc26f24a29ac6c4c))
* **tests:** use generic keywords for setup-knowledge-base test ([f21e4dd](https://github.com/etalab-ia/dragster/commit/f21e4dd17a7537e4403f1618710b04ae5b255c2b))


### Documentation

* add ASCII art logo to README ([b33b599](https://github.com/etalab-ia/dragster/commit/b33b5999c183b51b939b970ebe2e6935f5ae5be3))
* add ASCII art logo to README ([408e0d6](https://github.com/etalab-ia/dragster/commit/408e0d6dbecec20a91d8e691f13c9288e8eb2662))

## 0.1.0 (2026-03-23)


### Features

* add skills for document ingestion and search ([1cdf48c](https://github.com/etalab-ia/dragster/commit/1cdf48c8a098c5d3f3f55f2528a0e587c8dd1f05))
* ship dragster skills workflow (liteparse + qmd) ([2d324f2](https://github.com/etalab-ia/dragster/commit/2d324f2fcac0ee28792182fe9e51b0d9ad3b6b27))


### Bug Fixes

* move skills to skills/ directory, use official liteparse skill ([dff0450](https://github.com/etalab-ia/dragster/commit/dff045009f360c0090caf6016e144d8b73a04cc1))
* require KB storage details in setup skill responses ([72dca41](https://github.com/etalab-ia/dragster/commit/72dca41a091833d1b49db8d35119bbdb70989778))


### Documentation

* add release, license, and status badges to README ([e947d18](https://github.com/etalab-ia/dragster/commit/e947d189c8426cd2f73f98fa64410cdba4fde3f6))
* add release, license, and status badges to README ([9b90e12](https://github.com/etalab-ia/dragster/commit/9b90e127e95b371e2c38d098abc9a602667fbecd))
