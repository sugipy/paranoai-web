import { useState } from "react";
import { ActivityHeatmap } from "@/components/arc/activity-heatmap/activity-heatmap";
import activity from "@/data/activity.json";

/** ヒーロー右の「積み上げ」マス。データは tools/gen_activity.py が作る（日付と件数だけ）。 */
export default function Streak() {
  const [selected, setSelected] = useState<string | null>(null);
  return (
    <ActivityHeatmap
      days={activity.days}
      label="運営者がこの100日に積み上げた記録"
      period="この100日"
      unit={{ one: "件", other: "件" }}
      weekStartsOn={1}
      locale="ja-JP"
      selectedDate={selected}
      onSelectDate={setSelected}
    />
  );
}
