---
schema_version: will-ai-question-bank/v1
source_pdf: VFJVFK_R00_2023KW_C1N.pdf
source_sha256: 3e754c4b1ee0170819f5a30a6606315f71b3b9de48ae68fcc96bacd3230fd777
source_pages: 50
question_bank_version: V1
product_scope: VFJ / VFK
---

# VFJVFK_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `VFJVFK_R00_2023KW_C1N.pdf`
- SHA-256: `3e754c4b1ee0170819f5a30a6606315f71b3b9de48ae68fcc96bacd3230fd777`
- Physical pages: 50
- Product scope: VFJ 油压定位/弹簧释放型与 VFK 油压定位/油压释放型扩径定位销，以及 PDF 内直接适用的设计、安装、回路、操作和维护要求

## 2. Scope

本题库把 VFJ 与 VFK 作为同一份组合来源中的两个产品范围，覆盖型号语法、动作原理、D/C 定位功能、规格与能力、可定位工件重量计算、选配检测、安装相位、垂直使用、配管回路和直接适用的共通注意事项。公司介绍、销售网点、纯目录导航以及 VFL/VFM 等其他系列的专属规格不作为考核对象。

### 2.1 覆盖原则

- `HIGH`：型号、动作、规格、能力、检测、相位、安装、回路和失效后果均映射到题目。
- `MEDIUM`：直接适用于 VFJ/VFK 的液压施工、操作与维护要求映射到代表题。
- `LOW/EXCLUDED`：备忘空页、标示变更、公司与销售资料以及其他系列专属数据保留处置理由，不生成题目。

### 2.2 图表与计算边界

- 本 PDF 没有对 VFJ/VFK 给出可作为连续量 Gold 的性能曲线，因此不设置 `CHART` 题。
- 可定位工件重量使用 PDF 公式与规格表扩径力作确定性计算；最终值采用 `ROUND_HALF_UP` 精确到 0.01 kg，不附加伪容差。

### 2.3 来源清单

| Coverage ID | 物理页 | 局部范围 | Evidence type | 可测试对象 / 范围决定 | Priority / Disposition |
|---|---:|---|---|---|---|
| VFJVFK-SI-001 | 1-2 | 产品总览与系列比较 | TEXT + TABLE | 扩缩径、重复定位精度、驱动类型与检测选配；`VFJVFK-Q-0003`、`0010` | HIGH：已映射 |
| VFJVFK-SI-002 | 3-4 | 目录与 VFJ/VFK 动作原理 | STATE_DIAGRAM + TEXT | 两系列定位与释放顺序；`VFJVFK-Q-0003`-`0004` | HIGH：已映射 |
| VFJVFK-SI-003 | 5-6 | VFJ 型号表示 | MODEL + TABLE | VFJ 字段、选配项与供气口；`VFJVFK-Q-0001`、`0011` | HIGH：已映射 |
| VFJVFK-SI-004 | 7 | VFJ 规格与重量公式 | TABLE + FORMULA | VFJ 能力、共通规格与工件重量；`VFJVFK-Q-0005`、`0006`、`0008` | HIGH：已映射 |
| VFJVFK-SI-005 | 9-20 | VFJ 标准/B/M 外形尺寸 | DRAWING + TABLE + CAUTION | 安装、工件孔与检测型边界；`VFJVFK-Q-0011`、`0016` | HIGH：已映射 |
| VFJVFK-SI-006 | 21-22 | VFK 型号表示 | MODEL + TABLE | VFK 字段、孔径与选配兼容；`VFJVFK-Q-0002`、`0011` | HIGH：已映射 |
| VFJVFK-SI-007 | 23 | VFK 规格与重量公式 | TABLE + FORMULA | VFK 能力、共通规格与工件重量；`VFJVFK-Q-0005`、`0007`、`0009` | HIGH：已映射 |
| VFJVFK-SI-008 | 25-36 | VFK 标准/B/M 外形尺寸 | DRAWING + TABLE + CAUTION | 安装尺寸和检测型边界；`VFJVFK-Q-0011`、`0016` | HIGH：已映射 |
| VFJVFK-SI-009 | 37-40 | VFJ/VFK 设计与安装注意事项 | CAUTION + DRAWING + TABLE | 供气、相位、倾斜、薄壁孔、紧固与排气；`VFJVFK-Q-0012`-`0016` | HIGH：已映射 |
| VFJVFK-SI-010 | 41-42 | VFJ/VFK 参考回路 | PROCEDURE + CAUTION | 动作顺序、背压、流量与独立回路；`VFJVFK-Q-0017`-`0018` | HIGH：已映射 |
| VFJVFK-SI-011 | 43-46 | 液压系列通用施工、操作与维护 | PROCEDURE + CAUTION | 清洁、排气、安全与定检；`VFJVFK-Q-0019`-`0020` | MEDIUM：已映射 |
| VFJVFK-SI-012 | 47-48 | 标示变更附录 | TABLE + TEXT | 表面粗糙度与 O 形圈旧新标示 | LOW：不构成 VFJ/VFK 耐久产品题 |
| VFJVFK-SI-013 | 49-50 | 公司与销售网点 | TEXT | 联系方式与公司信息 | EXCLUDED：非耐久技术知识 |

## 3. Question Statistics

- Total: 20
- Direct VFJ/VFK: 19
- Document Common: 1
- MODEL: 2
- FACT: 2
- SPEC_LOOKUP: 2
- TABLE: 2
- CALCULATION: 2
- PROCEDURE: 5
- CAUTION: 5

## 4. Questions

## VFJVFK-Q-0001

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: VFJ 扩径定位销
- Model / Scope: `VFJ2000-080-D-H20-MR`

### Question

逐段解释型号 `VFJ2000-080-D-H20-MR` 中的系列、主体尺寸、设计编号、工件孔径符号、功能、着座高度、选配项和供气口位置。

### Standard Answer

`VFJ` 表示油压定位、弹簧释放的单动型扩径定位销；`2` 表示主体尺寸 2，可选 φ7.6～φ10.8 的直孔范围；`000` 中的设计编号为 0；`080` 对应直孔 φ7.6～φ8.5 或锥孔 φ8～φ8.5；`D` 是基准定位用基准销；`H20` 表示着座高度 20 mm；`M` 是释放动作确认型；`R` 表示供气口采用右图 R 位置。

### Scoring Standard

- P1 [10]: `VFJ` 正确识别为扩径定位销系列。
- P2 [10]: `VFJ` 的定位动力正确写为油压。
- P3 [10]: `VFJ` 的释放动力正确写为弹簧力。
- P4 [10]: 主体尺寸 `2` 正确对应直孔 φ7.6～φ10.8 的可选范围。
- P5 [10]: 设计编号正确写为 `0`。
- P6 [10]: `080` 的直孔范围正确写为 φ7.6～φ8.5。
- P7 [10]: `D` 正确解释为基准定位用基准销。
- P8 [10]: `H20` 正确解释为 20 mm 着座高度。
- P9 [10]: `M` 正确解释为释放动作确认型。
- P10 [10]: `R` 正确解释为供气口 R 位置。

### Accepted Variants

- “圆销定位”可作为 D 基准销功能的补充说法。

### Forbidden Errors

- 将 VFJ 说成油压释放，或将 M 说成着座确认型。

### Tolerance

- N/A

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 5-6
- Printed page: 1363-1364
- Section: VFJ 型号表示
- Local scope path: VFJ > 型号表示 > 字段 1 至 7
- Evidence type: MODEL
- Evidence: 型号示例、孔径表、功能分类、着座高度、选配项与供气口位置共同定义各字段。

## VFJVFK-Q-0002

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: VFK 扩径定位销
- Model / Scope: `VFK3000-130-C-H25-BL`

### Question

逐段解释型号 `VFK3000-130-C-H25-BL` 中的系列、主体尺寸、设计编号、工件孔径符号、功能、着座高度、选配项和供气口位置。

### Standard Answer

`VFK` 表示油压定位、油压释放的复动型扩径定位销；`3` 表示主体尺寸 3，可选 φ10.4～φ16.2 的直孔范围；设计编号为 0；`130` 对应直孔 φ12.2～φ14.1 或锥孔 φ13～φ14.1；`C` 是单一方向定位用菱形销；`H25` 表示着座高度 25 mm；`B` 是着座确认型；`L` 表示供气口采用右图 L 位置。

### Scoring Standard

- P1 [10]: `VFK` 正确识别为扩径定位销系列。
- P2 [10]: `VFK` 的定位动力正确写为油压。
- P3 [10]: `VFK` 的释放动力正确写为油压。
- P4 [10]: 主体尺寸 `3` 正确对应直孔 φ10.4～φ16.2 的可选范围。
- P5 [10]: 设计编号正确写为 `0`。
- P6 [10]: `130` 的直孔范围正确写为 φ12.2～φ14.1。
- P7 [10]: `C` 正确解释为单一方向定位用菱形销。
- P8 [10]: `H25` 正确解释为 25 mm 着座高度。
- P9 [10]: `B` 正确解释为着座确认型。
- P10 [10]: `L` 正确解释为供气口 L 位置。

### Accepted Variants

- “切边销”可作为 C 菱形销的同义说法。

### Forbidden Errors

- 将 VFK 说成弹簧释放，或将 B 说成释放动作确认型。

### Tolerance

- N/A

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 21-22
- Printed page: 1379-1380
- Section: VFK 型号表示
- Local scope path: VFK > 型号表示 > 字段 1 至 7
- Evidence type: MODEL
- Evidence: VFK 型号示例、主体尺寸/孔径表和选配项定义共同给出各字段含义。

## VFJVFK-Q-0003

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: VFJ / VFK 扩径定位销
- Model / Scope: 两系列驱动方式比较

### Question

VFJ 与 VFK 分别采用什么定位和释放方式？各自属于油压单动型还是油压复动型？

### Standard Answer

VFJ 由油压定位、弹簧力释放，属于油压单动型；VFK 由油压定位、油压释放，属于油压复动型。

### Scoring Standard

- P1 [17]: VFJ 正确写为油压定位。
- P2 [17]: VFJ 正确写为弹簧力释放。
- P3 [16]: VFJ 正确归类为油压单动型。
- P4 [17]: VFK 正确写为油压定位。
- P5 [17]: VFK 正确写为油压释放。
- P6 [16]: VFK 正确归类为油压复动型。

### Accepted Variants

- “弹簧复位”可作为 VFJ 弹簧释放的等价表述。

### Forbidden Errors

- 声称 VFJ 需要释放油压，或把 VFK 归为单动型。

### Tolerance

- N/A

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 3-4
- Printed page: 1361-1362
- Section: 动作原理
- Local scope path: VFJ/VFK > 动作原理 > 定位与释放驱动
- Evidence type: STATE_DIAGRAM
- Evidence: 动作剖视图分别标明 VFJ 的油压定位/弹簧释放和 VFK 的油压定位/油压释放。

## VFJVFK-Q-0004

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: VFJ / VFK 扩径定位销
- Model / Scope: 工件搬入、定位与搬出动作顺序

### Question

分别说明 VFJ 与 VFK 在工件搬入、定位以及搬出时的压力操作和内部动作。

### Standard Answer

搬入/搬出时，VFJ 撤除定位油压，活塞杆由释放弹簧下降，钢球自由；VFK 撤除定位油压并供给释放油压，活塞杆下降，钢球自由。定位时，两者均供给定位油压，使活塞杆上升并推动钢球扩径；VFK 还必须先解除释放油压。

### Scoring Standard

- P1 [8]: VFJ 搬入/搬出前撤除定位油压。
- P2 [8]: VFJ 搬入/搬出时释放弹簧使活塞杆下降。
- P3 [8]: VFJ 搬入/搬出时钢球处于自由状态。
- P4 [8]: VFK 搬入/搬出前撤除定位油压。
- P5 [8]: VFK 搬入/搬出时供给释放油压。
- P6 [8]: VFK 搬入/搬出时活塞杆下降。
- P7 [8]: VFK 搬入/搬出时钢球处于自由状态。
- P8 [8]: 定位时 VFJ 供给定位油压。
- P9 [9]: VFK 定位前解除释放油压。
- P10 [9]: VFK 定位时供给定位油压。
- P11 [9]: 定位时活塞杆上升。
- P12 [9]: 定位时钢球扩径。

### Accepted Variants

- 可把“钢球自由”表述为“不施加扩径定位力”。

### Forbidden Errors

- 在 VFK 定位时同时保持释放油压，或在 VFJ 搬出时继续供给定位油压。

### Tolerance

- N/A

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 4
- Printed page: 1362
- Section: 动作原理
- Local scope path: VFJ/VFK > 动作原理 > 工件搬入/搬出与定位
- Evidence type: STATE_DIAGRAM
- Evidence: 左右剖视图和步骤文字直接给出两系列压力状态、活塞杆方向与钢球状态。

## VFJVFK-Q-0005

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: VFJ / VFK 扩径定位销
- Model / Scope: 共通性能与压力范围比较

### Question

列出 VFJ 与 VFK 的重复定位精度、推荐喷气清洁气压和使用温度范围，并说明两系列的使用压力范围有何不同。

### Standard Answer

两系列重复定位精度均为 0.01 mm，推荐喷气清洁气压均为 0.3～0.4 MPa，使用温度范围均为 0～70 ℃。VFJ 的使用压力范围为 2.5～7.0 MPa；VFK2000-060/070 为 1.5～5.0 MPa，其余 VFK 表列型号为 1.5～7.0 MPa。

### Scoring Standard

- P1 [15]: VFJ 重复定位精度正确写为 0.01 mm。
- P2 [15]: VFK 重复定位精度正确写为 0.01 mm。
- P3 [15]: 推荐喷气清洁气压正确写为 0.3～0.4 MPa。
- P4 [15]: 使用温度范围正确写为 0～70 ℃。
- P5 [15]: VFJ 使用压力范围正确写为 2.5～7.0 MPa。
- P6 [15]: VFK2000-060/070 使用压力范围正确写为 1.5～5.0 MPa。
- P7 [10]: 其余 VFK 表列型号使用压力范围正确写为 1.5～7.0 MPa。

### Accepted Variants

- 10 μm 与 0.01 mm 等价。

### Forbidden Errors

- 把 VFK2000-060/070 的上限写成 7.0 MPa。

### Tolerance

- 必须给出表列范围与单位；不接受数值容差。

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 7, 23
- Printed page: 1365, 1381
- Section: VFJ/VFK 规格
- Local scope path: VFJ/VFK > 规格 > 共通性能与使用压力
- Evidence type: TABLE
- Evidence: 两张规格表分别列出重复定位精度、压力、喷气气压和温度范围。

## VFJVFK-Q-0006

**Type: SPEC_LOOKUP**

### Target

- Binding: EXACT_MODEL
- Product: VFJ 扩径定位销
- Model / Scope: `VFJ2000-090`

### Question

查表给出 `VFJ2000-090` 的直孔范围、锥孔范围、C 型容许偏心量、2.5/5.0/7.0 MPa 时扩径力、容许剪切载荷和空动时定位销容量。

### Standard Answer

直孔 φ8.5～φ9.5 mm；锥孔 φ9～φ9.5 mm；C 型容许偏心量 ±0.4 mm；扩径力在 2.5/5.0/7.0 MPa 时分别为 110/260/380 N；容许剪切载荷 600 N；空动时定位销容量 0.10 cm³。

### Scoring Standard

- P1 [10]: 直孔范围正确写为 φ8.5～φ9.5 mm。
- P2 [10]: 锥孔范围正确写为 φ9～φ9.5 mm。
- P3 [10]: C 型容许偏心量正确写为 ±0.4 mm。
- P4 [10]: 2.5 MPa 时扩径力正确写为 110 N。
- P5 [10]: 5.0 MPa 时扩径力正确写为 260 N。
- P6 [10]: 7.0 MPa 时扩径力正确写为 380 N。
- P7 [20]: 容许剪切载荷正确写为 600 N。
- P8 [20]: 空动时定位销容量正确写为 0.10 cm³。

### Accepted Variants

- 容量单位可写作 `cc`，但必须与 0.10 对应。

### Forbidden Errors

- 将 VFJ3000 的扩径力或剪切载荷代入本型号。

### Tolerance

- 必须精确命中表值与单位。

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1365
- Section: 规格：VFJ2000
- Local scope path: VFJ > 规格 > VFJ2000-090 列
- Evidence type: TABLE
- Evidence: VFJ2000-090 列直接给出孔径、偏心量、剪切载荷和容量，扩径力行为 VFJ2000 系列共通值。

## VFJVFK-Q-0007

**Type: SPEC_LOOKUP**

### Target

- Binding: EXACT_MODEL
- Product: VFK 扩径定位销
- Model / Scope: `VFK2000-060`

### Question

查表给出 `VFK2000-060` 的直孔范围、锥孔范围、C 型容许偏心量、1.5/5.0 MPa 时扩径力、容许剪切载荷、释放侧/定位侧空动容量、使用压力范围和耐压。

### Standard Answer

直孔 φ5.7～φ6.6 mm；锥孔 φ6.1～φ6.6 mm；C 型容许偏心量 ±0.25 mm；1.5/5.0 MPa 时扩径力分别为 90/300 N；容许剪切载荷 250 N；释放侧/定位侧空动容量分别为 0.03/0.08 cm³；使用压力范围 1.5～5.0 MPa；耐压 7.0 MPa。

### Scoring Standard

- P1 [10]: 直孔范围正确写为 φ5.7～φ6.6 mm。
- P2 [10]: 锥孔范围正确写为 φ6.1～φ6.6 mm。
- P3 [10]: C 型容许偏心量正确写为 ±0.25 mm。
- P4 [10]: 1.5 MPa 时扩径力正确写为 90 N。
- P5 [10]: 5.0 MPa 时扩径力正确写为 300 N。
- P6 [10]: 容许剪切载荷正确写为 250 N。
- P7 [10]: 释放侧空动容量正确写为 0.03 cm³。
- P8 [10]: 定位侧空动容量正确写为 0.08 cm³。
- P9 [10]: 使用压力范围正确写为 1.5～5.0 MPa。
- P10 [10]: 耐压正确写为 7.0 MPa。

### Accepted Variants

- 容量单位可写作 `cc`。

### Forbidden Errors

- 将 7.0 MPa 耐压误作允许连续使用压力。

### Tolerance

- 必须精确命中表值与单位。

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 23
- Printed page: 1381
- Section: 规格：VFK2000
- Local scope path: VFK > 规格 > VFK2000-060 列
- Evidence type: TABLE
- Evidence: VFK2000-060 列和系列共通行直接给出全部查表量。

## VFJVFK-Q-0008

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: VFJ 扩径定位销
- Model / Scope: `VFJ3000`，5.0 MPa，水平平置，μ=0.20

### Question

一台 `VFJ3000` 在 5.0 MPa 下水平平置使用，工件着座面摩擦系数 μ=0.20。按 PDF 公式和效率 0.25，计算最大可定位工件重量，结果用 `ROUND_HALF_UP` 保留 0.01 kg，并写出代入式。

### Standard Answer

规格表给出扩径力 F=580 N。代入 `W ≤ F×0.25/(μ×9.8)`：`W ≤ 580×0.25/(0.20×9.8)=73.979591... kg`，按 `ROUND_HALF_UP` 保留 0.01 kg 得 `73.98 kg`。

### Scoring Standard

- P1 [15]: 正确查得 5.0 MPa 时扩径力 F=580 N。
- P2 [15]: 正确使用水平平置公式 `W ≤ F×效率/(μ×9.8)`。
- P3 [10]: 正确代入效率 0.25。
- P4 [10]: 正确代入摩擦系数 μ=0.20。
- P5 [10]: 正确代入重力换算常数 9.8。
- P6 [15]: 正确得到未舍入值约 73.979591 kg。
- P7 [15]: 正确按 `ROUND_HALF_UP` 得到 73.98。
- P8 [10]: 最终答案明确写出单位 kg。

### Accepted Variants

- 代数等价且中间精度足以得到 73.98 kg 的写法均可。

### Forbidden Errors

- 使用垂直挂壁公式而漏掉 μ，或使用 VFK3000 的 650 N。

### Tolerance

- 最终值必须按指定规则精确舍入为 73.98 kg。

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1365
- Section: VFJ3000 规格；扩径力与可定位工件重量关系式
- Local scope path: VFJ > 规格 > VFJ3000 5.0 MPa 行；水平姿势公式
- Evidence type: FORMULA + TABLE
- Evidence: 规格表给出 580 N，页面下方给出含 μ、9.8 与效率 0.25 的水平公式。

## VFJVFK-Q-0009

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: VFK 扩径定位销
- Model / Scope: `VFK3000`，5.0 MPa，垂直挂壁

### Question

一台 `VFK3000` 在 5.0 MPa 下垂直挂壁使用。按 PDF 公式和效率 0.25，计算最大可定位工件重量，结果用 `ROUND_HALF_UP` 保留 0.01 kg，并写出代入式。

### Standard Answer

规格表给出扩径力 F=650 N。代入 `W ≤ F/9.8×0.25`：`W ≤ 650/9.8×0.25=16.581632... kg`，按 `ROUND_HALF_UP` 保留 0.01 kg 得 `16.58 kg`。

### Scoring Standard

- P1 [15]: 正确查得 5.0 MPa 时扩径力 F=650 N。
- P2 [15]: 正确使用垂直挂壁公式 `W ≤ F/9.8×效率`。
- P3 [15]: 正确代入效率 0.25。
- P4 [15]: 正确代入重力换算常数 9.8。
- P5 [15]: 正确得到未舍入值约 16.581632 kg。
- P6 [15]: 正确按 `ROUND_HALF_UP` 得到 16.58。
- P7 [10]: 最终答案明确写出单位 kg。

### Accepted Variants

- `650×0.25/9.8` 与标准代入式等价。

### Forbidden Errors

- 在垂直公式中引入未给定摩擦系数，或使用 VFJ3000 的 580 N。

### Tolerance

- 最终值必须按指定规则精确舍入为 16.58 kg。

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 23
- Printed page: 1381
- Section: VFK3000 规格；扩径力与可定位工件重量关系式
- Local scope path: VFK > 规格 > VFK3000 5.0 MPa 行；垂直姿势公式
- Evidence type: FORMULA + TABLE
- Evidence: 规格表给出 650 N，页面下方给出除以 9.8 并乘效率 0.25 的垂直公式。

## VFJVFK-Q-0010

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: VFJ / VFK 扩径定位销
- Model / Scope: D 基准销与 C 菱形销定位功能

### Question

D 型与 C 型分别承担什么定位功能？图示中钢球作用部位数量分别是多少？

### Standard Answer

D 型为基准定位用基准销，通过 3 个钢球作用部位约束基准位置；C 型为单一方向定位用菱形销，通过 2 个相对的钢球作用部位约束一个方向。

### Scoring Standard

- P1 [25]: D 型正确识别为基准定位用基准销。
- P2 [25]: D 型正确写为 3 个钢球作用部位。
- P3 [25]: C 型正确识别为单一方向定位用菱形销。
- P4 [25]: C 型正确写为 2 个相对钢球作用部位。

### Accepted Variants

- D 型可称圆销，C 型可称切边销。

### Forbidden Errors

- 声称 C 型可独立完成全部平面定位约束。

### Tolerance

- N/A

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 4-5, 21
- Printed page: 1362-1363, 1379
- Section: 关于基准定位和单个方向定位；功能分类
- Local scope path: VFJ/VFK > 动作原理/型号表示 > D/C 功能
- Evidence type: DRAWING + TEXT
- Evidence: 动作页和两系列型号页一致标示 D 的 3 部位与 C 的 2 部位及各自定位用途。

## VFJVFK-Q-0011

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: VFJ / VFK 扩径定位销
- Model / Scope: B/M 检测选配与供气口兼容边界

### Question

说明 B、M 与无符号各表示什么；VFK2000-060/070 能否选 B/M；何时才需要 R/L 供气口位置，并说明 B 与 M 同时使用的处理要求。

### Standard Answer

无符号为标准无检测型，B 为着座确认型，M 为释放动作确认型。VFK2000-060/070 仅支持无符号，不能选 B/M；VFJ 与 VFK080～150 的适用型号可按表选 B 或 M。只有选择 B 或 M 时才指定 R/L 供气口位置。B 与 M 组合使用需另行询问厂家。

### Scoring Standard

- P1 [12]: 无符号正确解释为标准无检测型。
- P2 [12]: B 正确解释为着座确认型。
- P3 [12]: M 正确解释为释放动作确认型。
- P4 [16]: VFK2000-060/070 正确写为不能选 B。
- P5 [16]: VFK2000-060/070 正确写为不能选 M。
- P6 [12]: R/L 正确限定为选择 B 或 M 时使用。
- P7 [10]: R/L 正确解释为供气口位置。
- P8 [10]: B 与 M 组合使用正确写为需另行询问厂家。

### Accepted Variants

- “无传感确认”可作为无符号标准型的补充说明。

### Forbidden Errors

- 为 VFK2000-060/070 配置 B 或 M，或把 R/L 当作功能分类字段。

### Tolerance

- N/A

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 6, 22
- Printed page: 1364, 1380
- Section: 选配项；供气口位置
- Local scope path: VFJ/VFK > 型号表示 > 字段 6/7
- Evidence type: TABLE + DRAWING
- Evidence: 选配表定义无符号/B/M 与 VFK060/070 边界，供气图限定 R/L 的适用条件。

## VFJVFK-Q-0012

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VFJ / VFK 扩径定位销
- Model / Scope: 喷气清洁与检测供气连续性

### Question

VFJ/VFK 使用时，喷气清洁口以及 B/M 检测口的供气应如何保持？中断供气的主要后果是什么？

### Standard Answer

喷气清洁用供气口应始终连续供给清洁空气，防止异物进入装置内部；B 型应始终向着座确认口供气，M 型应始终向释放动作确认口供气。中断后继续使用可能使异物侵入并导致定位销动作异常；检测口断气还会使相应确认功能失效。

### Scoring Standard

- P1 [17]: 喷气清洁口正确要求连续供气。
- P2 [17]: 连续喷气目的正确写为防止异物进入内部。
- P3 [17]: B 型正确要求持续向着座确认口供气。
- P4 [17]: M 型正确要求持续向释放动作确认口供气。
- P5 [16]: 喷气中断后果正确写为可能导致动作异常。
- P6 [16]: 检测口断气后果正确写为相应确认功能失效。

### Accepted Variants

- “不停气”与“始终供气”等价。

### Forbidden Errors

- 把喷气清洁仅作为周期性短脉冲，或允许 B/M 正常运行时关闭检测供气。

### Tolerance

- N/A

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 37
- Printed page: 1395
- Section: 设计方面的注意事项—关于供气
- Local scope path: VFJ/VFK > 注意事项 > 供气
- Evidence type: CAUTION
- Evidence: 页面明确要求清洁口、B 着座确认口与 M 释放确认口始终供气并说明异物侵入后果。

## VFJVFK-Q-0013

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VFJ / VFK 扩径定位销
- Model / Scope: D/C 安装相位与 Z 轴基准面

### Question

成对使用 D 基准销和 C 菱形销时，C 的扩径方向应如何设定？标准/M 型与 B 型在 Z 轴基准面设置上有何不同？

### Standard Answer

C 菱形销应以 D 基准销为基准调整相位，使 C 的扩径方向垂直于 D/C 中心连线。B 型在法兰上面自带着座，可作为 Z 轴方向基准面；标准型和 M 型没有着座，必须由用户另行设置 Z 轴方向定位着座面。

### Scoring Standard

- P1 [25]: 正确写出 C 的相位以 D 为基准调整。
- P2 [25]: 正确写出 C 扩径方向垂直于 D/C 中心连线。
- P3 [25]: 正确写出 B 型法兰上面自带着座。
- P4 [25]: 正确写出标准/M 型需另设 Z 轴定位着座面。

### Accepted Variants

- “90°”可替代“垂直”。

### Forbidden Errors

- 让 C 的扩径方向平行于 D/C 中心连线，或声称标准型自带 Z 向着座。

### Tolerance

- N/A

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 37
- Printed page: 1395
- Section: 关于安装方向（相位）；关于 Z 轴方向的基准面
- Local scope path: VFJ/VFK > 设计注意事项 > 相位与 Z 轴基准
- Evidence type: DRAWING + CAUTION
- Evidence: D/C 平面图标出垂直扩径方向，侧视图比较 B 型自带着座与标准/M 型另设着座。

## VFJVFK-Q-0014

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VFJ / VFK 扩径定位销
- Model / Scope: 垂直挂壁与倾斜工件防损

### Question

垂直挂壁或倾斜搬入/搬出工件时，PDF 要求采取哪些防损措施，并给出定位销倾斜度控制范围和更换条件。

### Standard Answer

应避免工件浮起或倾斜后直接定位，先用预夹紧装置压紧；垂直使用会使内部滑动面偏磨，应定期确认定位精度，超出容许范围约 2～3° 时立即更换。扩径定位销相对工件的倾斜度应控制在 4/100～5/100；倾斜状态搬入/搬出尤其易损坏，应设置粗导销引导。

### Scoring Standard

- P1 [15]: 正确要求避免浮起或倾斜状态直接定位。
- P2 [15]: 正确要求先用预夹紧装置压紧工件。
- P3 [15]: 正确指出垂直使用会造成内部滑动面偏磨。
- P4 [15]: 正确要求定期确认定位精度。
- P5 [10]: 更换条件正确写为超出约 2～3° 容许范围。
- P6 [15]: 倾斜度控制范围正确写为 4/100～5/100。
- P7 [15]: 正确要求设置粗导销引导搬入/搬出。

### Accepted Variants

- “导向销”与“粗导销”在明确为搬入/搬出引导时等价。

### Forbidden Errors

- 允许倾斜工件直接落到扩径部位，或把 2～3° 当作正常目标倾角。

### Tolerance

- 必须给出 PDF 的范围；不接受扩展范围。

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 38
- Printed page: 1396
- Section: 垂直姿势使用；关于 Z 轴方向的倾斜度
- Local scope path: VFJ/VFK > 注意事项 > 垂直与倾斜工件
- Evidence type: CAUTION + DRAWING
- Evidence: 页面文字和正误图直接给出预夹紧、偏磨、更换、倾斜度及粗导销要求。

## VFJVFK-Q-0015

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VFJ / VFK 扩径定位销
- Model / Scope: 工件孔薄壁变形与孔距误差预算

### Question

薄壁工件孔与 VFJ/VFK 的 D/C 孔距设计分别有什么风险和预算原则？

### Standard Answer

薄壁工件孔在扩径时可能变形，导致无法达到规定定位精度，因此正式使用前必须做动作测试。VFJ/VFK 的 D/C 安装孔间距及工件孔间距精度必须在考虑 C 菱形销容许偏心量的基础上加工，不能直接套用 VFL/VFM 的 ±0.02 mm 单项规则。

### Scoring Standard

- P1 [25]: 正确指出薄壁孔扩径时可能变形。
- P2 [25]: 正确指出变形会导致规定定位精度无法达到。
- P3 [25]: 正确要求正式使用前进行动作测试。
- P4 [25]: VFJ/VFK 孔距误差预算正确要求纳入 C 型容许偏心量。

### Accepted Variants

- “试动作/实机验证”可作为动作测试的等价表述。

### Forbidden Errors

- 把 VFL/VFM 的 ±0.02 mm 直接作为 VFJ/VFK 唯一孔距判定式。

### Tolerance

- N/A

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 38-39
- Printed page: 1396-1397
- Section: 工件孔周围壁厚；关于 VFJ/VFK 之间的间距精度
- Local scope path: VFJ/VFK > 注意事项 > 薄壁孔与孔距精度
- Evidence type: CAUTION + TEXT
- Evidence: 薄壁孔段给出变形风险，VFJ/VFK 专属段要求在容许偏心量基础上加工 D/C 与工件孔距。

## VFJVFK-Q-0016

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: VFJ / VFK 扩径定位销
- Model / Scope: 安装紧固、排气口与 O 形密封圈

### Question

说明 VFJ/VFK 安装时的紧固方法、扭矩、禁用垫圈、M 型排气口处置以及 O 形密封圈安装顺序。

### Standard Answer

两系列均用 2 根 M5×0.8、强度等级 12.9 的安装螺栓均匀紧固，紧固扭矩为 6.3 N·m；不得使用弹簧垫圈或带齿垫圈。M 型排气口应避开冷却液/切屑，优先板式深孔移位，受冷却影响时采用外部配管移至安全位置。安装 VFJ/VFK 本体前，应先把随附 O 形密封圈装入夹具侧安装孔，再安装本体。

### Scoring Standard

- P1 [9]: 正确写出 2 根安装螺栓。
- P2 [9]: 螺纹规格正确写为 M5×0.8。
- P3 [9]: 螺栓强度等级正确写为 12.9。
- P4 [9]: 正确要求均匀紧固。
- P5 [9]: 紧固扭矩正确写为 6.3 N·m。
- P6 [9]: 正确禁止弹簧垫圈。
- P7 [9]: 正确禁止带齿垫圈。
- P8 [9]: M 型排气口正确要求避开冷却液。
- P9 [9]: M 型排气口正确要求避开切屑。
- P10 [9]: 受影响时正确要求用外部配管移位。
- P11 [10]: O 形圈正确要求先装入夹具侧安装孔再装本体。

### Accepted Variants

- “齿形垫圈”与“带齿垫圈”等价。

### Forbidden Errors

- 把 O 形圈先套在本体外侧再压入，或用弹簧垫圈防松。

### Tolerance

- 扭矩必须为 6.3 N·m；不接受数值容差。

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 40
- Printed page: 1398
- Section: 安装施工方面的注意事项
- Local scope path: VFJ/VFK > 注意事项 > 安装、排气与 O 形圈
- Evidence type: PROCEDURE + TABLE
- Evidence: 安装页的扭矩表和正误图直接给出螺栓、垫圈、排气口及 O 形圈顺序。

## VFJVFK-Q-0017

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: VFJ 扩径定位销
- Model / Scope: VFJ 标准/B/M 参考回路

### Question

按 VFJ 参考回路，说明定位紧固的动作顺序、独立回路要求、背压限制、喷气/检测气压和避免脉冲高压的方法。

### Standard Answer

定位紧固顺序应为 VFJ 扩径定位销先动作，再动作其他执行元件；扩径定位销与其他执行元件原则上各自独立回路。油箱回油管存在背压时，推荐把回油压力控制在小于 0.04 MPa。喷气清洁推荐 0.3～0.4 MPa，B/M 检测推荐 0.2 MPa，并配推荐 5 μm 过滤器。应调节流量避免脉冲高压；回路图中还要求定位销紧固时再动作其他元件。

### Scoring Standard

- P1 [14]: 动作顺序正确写为 VFJ 先定位。
- P2 [14]: 动作顺序正确写为其他执行元件随后动作。
- P3 [14]: 正确要求定位销与其他执行元件采用独立回路。
- P4 [14]: 回油背压限制正确写为小于 0.04 MPa。
- P5 [11]: 喷气清洁推荐气压正确写为 0.3～0.4 MPa。
- P6 [11]: B/M 检测推荐气压正确写为 0.2 MPa。
- P7 [11]: 过滤精度正确写为推荐 5 μm。
- P8 [11]: 正确要求调节流量以避免脉冲高压。

### Accepted Variants

- “分别独立”与“各自独立回路”等价。

### Forbidden Errors

- 让夹紧元件在 VFJ 定位前夹紧，或允许回油背压达到/超过 0.04 MPa。

### Tolerance

- 压力和过滤精度必须命中 PDF 标示值。

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 41
- Printed page: 1401
- Section: VFJ 参考回路范例
- Local scope path: VFJ > 注意事项 > 定位销与速度控制回路
- Evidence type: PROCEDURE + SCHEMATIC
- Evidence: VFJ 标准/B/M 三组回路和脚注共同给出动作顺序、独立回路、气压、过滤、背压及流量要求。

## VFJVFK-Q-0018

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: VFK 扩径定位销
- Model / Scope: VFK 标准/B/M 参考回路

### Question

按 VFK 参考回路，说明定位/释放油路、定位紧固顺序、独立回路、背压限制和气路要求。

### Standard Answer

VFK 是复动型，必须分别设置定位油压与释放油压；定位紧固顺序应为 VFK 先定位，再动作其他执行元件。扩径定位销与其他执行元件原则上各自独立回路；油箱回油管有背压时推荐回油压力小于 0.04 MPa，并调节流量避免脉冲高压。喷气清洁推荐 0.3～0.4 MPa，B/M 检测推荐 0.2 MPa，过滤器推荐 5 μm。

### Scoring Standard

- P1 [12]: 正确写出 VFK 需要定位油压油路。
- P2 [12]: 正确写出 VFK 需要释放油压油路。
- P3 [12]: 动作顺序正确写为 VFK 先定位。
- P4 [12]: 动作顺序正确写为其他执行元件随后动作。
- P5 [12]: 正确要求定位销与其他执行元件采用独立回路。
- P6 [10]: 回油背压限制正确写为小于 0.04 MPa。
- P7 [10]: 正确要求调节流量避免脉冲高压。
- P8 [10]: 喷气清洁推荐气压正确写为 0.3～0.4 MPa。
- P9 [5]: B/M 检测推荐气压正确写为 0.2 MPa。
- P10 [5]: 过滤精度正确写为推荐 5 μm。

### Accepted Variants

- 定位/释放油路可称 A/B 油路，但必须清楚对应功能。

### Forbidden Errors

- 把 VFK 画成弹簧释放单油路，或让夹紧先于定位。

### Tolerance

- 压力和过滤精度必须命中 PDF 标示值。

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 42
- Printed page: 1402
- Section: VFK 参考回路范例
- Local scope path: VFK > 注意事项 > 定位销与速度控制回路
- Evidence type: PROCEDURE + SCHEMATIC
- Evidence: VFK 标准/B/M 三组回路和脚注直接显示定位/释放油路、动作顺序及气液压边界。

## VFJVFK-Q-0019

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: VFJ / VFK 扩径定位销
- Model / Scope: VFJVFK_R00_2023KW_C1N.pdf :: 液压施工与回路排气

### Question

液压施工投用前应怎样清洁和缠绕密封带？若回路混入大量空气，应按什么顺序排气？

### Standard Answer

配管、接头、夹具油孔等必须彻底清洗后再投入使用；密封带从接头顶部保留 1～2 个螺纹牙再缠绕，且不得让残带进入回路。大量空气混入时：先把供油压力调到 2 MPa 以下；松开离夹紧器/支撑器最近的接头螺母一圈；左右摇动配管排出混气液压油；空气排净后重新紧固；必要时在最高或末端附近设置排气阀。

### Scoring Standard

- P1 [8]: 正确要求配管彻底清洗。
- P2 [8]: 正确要求接头彻底清洗。
- P3 [8]: 正确要求夹具油孔彻底清洗。
- P4 [8]: 密封带正确要求保留顶部 1～2 个螺纹牙。
- P5 [8]: 正确禁止残留密封带进入回路。
- P6 [8]: 排气前供油压力正确调至 2 MPa 以下。
- P7 [8]: 正确松开最近接头螺母一圈。
- P8 [8]: 正确通过左右摇动配管排出混气液压油。
- P9 [9]: 空气排净后正确重新紧固接头螺母。
- P10 [9]: 正确提出最高或末端附近设置排气阀。
- P11 [9]: 正确指出大量空气会使动作时间异常延长。
- P12 [9]: 正确保持施工环境清洁以防异物进入。

### Accepted Variants

- “2 MPa 或更低”与“2 MPa 以下”按安全方向等价接受。

### Forbidden Errors

- 在高压状态松接头排气，或把密封带缠到接头端面。

### Tolerance

- 压力上限和螺纹牙数必须与 PDF 一致。

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 43
- Printed page: 1725
- Section: 安装施工方面的注意事项（油压系列通用）
- Local scope path: 通用注意事项 > 液压施工 > 清洁、密封带与排气
- Evidence type: PROCEDURE
- Evidence: 页面逐项列出清洁、密封带缠绕和五步排气作业。

## VFJVFK-Q-0020

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: VFJ / VFK 扩径定位销
- Model / Scope: 操作安全与保养检查

### Question

概述 VFJ/VFK 拆卸前、重启前和日常保养中的关键安全检查要求。

### Standard Answer

拆卸前必须确认防坠落/防误动作措施已落实，切断压力源和电源，并确认油压、气压回路压力为零；高温设备须完全降温后再拆。重启前检查螺栓等连接部位无异常。日常应定期清扫活塞杆、柱塞周围和各基准/着座面，防止污物损伤密封并造成动作异常或漏油；定期检查配管、安装螺栓、螺母、固定环和夹紧器是否松动，检查液压油老化及装置动作是否正常顺畅。

### Scoring Standard

- P1 [7]: 拆卸前正确要求落实防坠落措施。
- P2 [7]: 拆卸前正确要求落实防误动作措施。
- P3 [7]: 拆卸前正确要求切断压力源。
- P4 [7]: 拆卸前正确要求切断电源。
- P5 [7]: 拆卸前正确确认油压回路压力为零。
- P6 [7]: 拆卸前正确确认气压回路压力为零。
- P7 [7]: 高温设备正确要求完全降温后再拆。
- P8 [7]: 重启前正确检查螺栓等连接部位。
- P9 [7]: 正确要求定期清扫活塞杆/柱塞周围。
- P10 [7]: 正确要求定期清扫基准/着座面。
- P11 [7]: 正确要求定期检查配管松动。
- P12 [7]: 正确要求定期检查紧固件松动。
- P13 [8]: 正确要求检查液压油老化。
- P14 [8]: 正确要求检查装置动作是否正常顺畅。

### Accepted Variants

- “断压、断电、泄压至零”可作为对应三项要求的概括，但评分仍逐项判定。

### Forbidden Errors

- 在残压未释放时拆卸，或允许污物附着的基准面继续使用。

### Tolerance

- N/A

### Source

- PDF: VFJVFK_R00_2023KW_C1N.pdf
- Physical page: 45-46
- Printed page: 1727-1728
- Section: 操作方面的注意事项；保养、检查
- Local scope path: 通用注意事项 > 安全操作与保养检查
- Evidence type: CAUTION + PROCEDURE
- Evidence: 两页直接列出拆卸隔离、降温、重启确认、清洁、松动、油液与动作检查要求。
