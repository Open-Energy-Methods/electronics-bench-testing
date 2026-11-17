/* EBT-MEC-020 - EDITABLE OPENSCAD CONCEPT MODEL
NOT FOR MANUFACTURE OR ENERGIZED TESTING.
Catalog sink envelope 100x100x40 mm, nominal base 10 mm.
Fin geometry, heater z/lead geometry, sensor markers are VISUAL SURROGATES.
*/
adapter = false;                 // true = OPTIONAL/unverified 4mm plate
show_both_heater_sites = true;  // alternative sites; NEVER power both in one run
show_sensor_markers = true;
projection_mode = false;
sink_x=100; sink_y=100; sink_z=40; base_z=10;
surrogate_fin_count=11; surrogate_fin_width=2.2;
adapter_z=4; heater_x=10.1; heater_y=14.6;
heater_visual_z=4; site_pitch=50;
$fn=36;
module sink_simplified() {
  color([0.37,0.45,0.50]) {
    translate([-sink_x/2,-sink_y/2,0]) cube([sink_x,sink_y,base_z]);
    for(i=[0:surrogate_fin_count-1]) {
      x=-sink_x/2+(i+0.5)*sink_x/surrogate_fin_count;
      translate([x-surrogate_fin_width/2,-sink_y/2,base_z])
        cube([surrogate_fin_width,sink_y,sink_z-base_z]);
    }
  }
}
module plate_unreleased() {
  color([0.79,0.57,0.32,0.92])
    translate([-50,-50,-adapter_z]) cube([100,100,adapter_z]);
}
module heater_at(x) {
  zbottom=adapter ? -adapter_z-heater_visual_z : -heater_visual_z;
  // visual body only; no certified package/fastener envelope
  color([0.16,0.21,0.25])
    translate([x-heater_x/2,-heater_y/2,zbottom])
      cube([heater_x,heater_y,heater_visual_z]);
  color([0.83,0.84,0.87])
    for(sign=[-1,1])
      translate([x+sign*3,heater_y/2,zbottom+1.2])
         cube([1.5,8,1.5]);
}
module sensor_marker(x,y) {
  color([0.13,0.76,0.70])
    translate([x,y,adapter ? -adapter_z-0.7 : -0.7])
      sphere(r=1.8);
}
module assembly() {
  sink_simplified();
  if(adapter) plate_unreleased();
  if(show_both_heater_sites) {
    heater_at(-site_pitch/2); heater_at(site_pitch/2);
  } else heater_at(-site_pitch/2);
  if(show_sensor_markers) {
    sensor_marker(-25,-17); sensor_marker(25,-17); sensor_marker(0,32);
  }
}
if(projection_mode) projection(cut=false) assembly();
else assembly();
