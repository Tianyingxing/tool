#!/bin/bash

# 轻量级多时区数字时钟
# 占用资源少，代码简洁

# 颜色定义
RED='\033[31m'
GREEN='\033[32m'
BLUE='\033[34m'
CYAN='\033[36m'
YELLOW='\033[33m'
MAGENTA='\033[35m'
BOLD='\033[1m'
RESET='\033[0m'

# 时区列表 (可自定义)
ZONES=(
    "Asia/Shanghai:上海"
    "America/New_York:纽约"
    "Europe/London:伦敦"
    "Asia/Tokyo:东京"
)

trap "tput cnorm; exit" INT
tput civis  # 隐藏光标

while true; do
    clear
    echo -e "${CYAN}${BOLD}═══════════════════════════════════════${RESET}"
    echo -e "${CYAN}${BOLD}     🕐 全球时钟${RESET}"
    echo -e "${CYAN}${BOLD}═══════════════════════════════════════${RESET}\n"
    
    for zone in "${ZONES[@]}"; do
        tz="${zone%:*}"
        city="${zone#*:}"
        time=$(TZ="$tz" date "+%H:%M:%S")
        date=$(TZ="$tz" date "+%m-%d")
        printf "%-12s  ${YELLOW}%s${RESET}  ${GREEN}%s${RESET}\n" "$city" "$time" "$date"
    done
    
    echo ""
    echo -e "${MAGENTA}本地: $(date '+%H:%M:%S')${RESET}"
    sleep 1
done
