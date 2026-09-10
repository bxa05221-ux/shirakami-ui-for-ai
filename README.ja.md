# shirakami-ui-for-ai

UI for AI — 人間のLandscapeとAIとの相互作用の境界を実装するためのプロジェクト。

## 位置づけ

`shirakami-OS` はRuntime基盤。

`shirakami-ui-for-ai` は、人間のLandscapeとAIとの相互作用の間に置かれ、Runtimeへ入る前の文脈を準備し、保持する観測境界。

概念的な流れ：

`Human Landscape → Observation Boundary → Shirakami Runtime → AI Adapter`

## 最初の実装目標

最初の目標は意図的に小さくする。

> Observation Contextを保持しながら、観測結果をその人や世界についての断定に変えない。

実装では、少なくとも次を保持する。

- 観測条件
- 観測された結果
- 不確実性／未解決状態
- Runtimeへ渡すために必要な系譜情報

## 境界ルール

- このリポジトリで新しいProtocol意味論を発明しない。
- 採用する理論は、正式な研究引継ぎ（`的目yaml`）を根拠とする。
- 観測は真実ではない。
- 一回の観測を、本質や人格の判断にしない。
- 分からない文脈は、分からないまま保持する。
- AIにはドメイン上の真実を宣言する権限を持たせない。
- `shirakami-OS` はRuntime境界として維持する。

## 開発順序

1. Observation Boundary Design
2. 最小限の観測データ構造
3. 条件と結果の分離を検証するテスト
4. Runtimeへの引き渡し統合
5. 正式採用後に、観測経路／レンズの実装へ進む

## ステータス

初期リポジトリ。Design-firstの実装段階。

## English

[README.md](README.md)
