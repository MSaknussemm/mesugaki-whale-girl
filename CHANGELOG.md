# 更新记录

## v1.0.0 — 2026-11-04

首个版本。61 段动画，角色 ID `mesugaki`。

- 分类：`idle` 6 / `random` 43 / `click` 8 / `move` 2 / `turn` 1 / `drag` 1（`events` 为空）
- 全部 640×360、24 fps、VP9 Profile 0、`yuva420p`（alpha_mode=1）
- `manifest.json`：`body_box [220,16,420,351]`、`head_box [214,16,426,156]`
- `move_strides.json`：`漂浮踏步` stride 90、`左转奔跑` stride 220
- Windows 安装脚本 `install.ps1`：自动定位安装目录、备份旧角色、支持 `-Uninstall` 还原；
  检测到旧项目的 `bluewhale_tv` 时只提示、不自动删
- 素材自检脚本 `tools/check_pack.py`

### 与 mesugaki-feiyu-pet 的差异

本项目是同一批动画的**完整版重新发布**，旧项目（47 段精选版，角色 ID `bluewhale_tv`）保持不动。

- 新增 14 段：`random/` 12 段（`可爱动作`、`戳屏幕`、`托腮思考`、`扭动挑衅`、`向前挥拳`、`暴躁跳跃`、`烦躁跺脚`、`短促跺脚`、`猫爪抓`、`拿出米饭`、`挤眉弄眼`、`吃光白米饭`）、
  `click/` 2 段（`点击回应-吃光白米饭`、`点击回应-电击抽搐`）
- 3 段在旧项目里是**改名后的同一素材**（字节相同）：
  `点击回应-吃白饭` → `random/喝水`、`点击回应-头发散乱` → `random/吹风`、`random/白米饭` → `random/啥也没有`
- `click/点击回应-被按墙上.webm` 与旧项目不是同一版剪辑（本版 601 KB / 旧版 1.03 MB）
