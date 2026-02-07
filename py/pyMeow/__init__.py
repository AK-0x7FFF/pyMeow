from __future__ import annotations
from typing import TypedDict

from .pyMeow import *
__all__ = ['NimPyException', '_Color', '_Module', '_Page', '_Pixel', '_Process', '_Rectangle', '_Texture', '_Vector2', '_Vector3', 'all_colors', 'allocate_memory', 'aob_scan_bytes', 'aob_scan_module', 'aob_scan_range', 'begin_drawing', 'bytes_to_string', 'check_collision_circle_rec', 'check_collision_circles', 'check_collision_lines', 'check_collision_point_rec', 'check_collision_recs', 'close_process', 'compare_color_pct', 'create_remote_thread', 'draw_circle', 'draw_circle_lines', 'draw_circle_sector', 'draw_circle_sector_lines', 'draw_ellipse', 'draw_ellipse_lines', 'draw_font', 'draw_fps', 'draw_line', 'draw_pixel', 'draw_poly', 'draw_poly_lines', 'draw_rectangle', 'draw_rectangle_lines', 'draw_rectangle_rounded', 'draw_rectangle_rounded_lines', 'draw_ring', 'draw_ring_lines', 'draw_text', 'draw_texture', 'draw_triangle', 'draw_triangle_lines', 'end_drawing', 'enum_memory_regions', 'enum_modules', 'enum_processes', 'fade_color', 'free_memory', 'get_color', 'get_display_resolution', 'get_fps', 'get_module', 'get_monitor_count', 'get_monitor_name', 'get_monitor_refresh_rate', 'get_os_error', 'get_proc_address', 'get_process_id', 'get_process_name', 'get_process_path', 'get_screen_height', 'get_screen_width', 'get_window_handle', 'get_window_info', 'get_window_position', 'get_window_title', 'gui_button', 'gui_check_box', 'gui_color_bar_alpha', 'gui_color_bar_hue', 'gui_color_picker', 'gui_combo_box', 'gui_dropdown_box', 'gui_fade', 'gui_group_box', 'gui_label', 'gui_label_button', 'gui_line', 'gui_load_style', 'gui_message_box', 'gui_panel', 'gui_progress_bar', 'gui_scroll_bar', 'gui_set_state', 'gui_slider', 'gui_slider_bar', 'gui_spinner', 'gui_status_bar', 'gui_text_box', 'gui_window_box', 'inject_library', 'inject_shellcode', 'is_64_bit', 'is_sound_playing', 'key_pressed', 'load_font', 'load_sound', 'load_texture', 'load_texture_bytes', 'measure_font', 'measure_text', 'module_exists', 'mouse_click', 'mouse_down', 'mouse_move', 'mouse_position', 'mouse_pressed', 'mouse_up', 'new_color', 'new_color_float', 'new_color_hex', 'open_process', 'overlay_close', 'overlay_init', 'overlay_loop', 'page_protection', 'pause_sound', 'pid_exists', 'pixel_at_mouse', 'pixel_enum_region', 'pixel_enum_screen', 'pixel_save_to_file', 'pixel_search_colors', 'play_multisound', 'play_sound', 'pointer_chain_32', 'pointer_chain_64', 'press_key', 'process_exists', 'process_running', 'r', 'r_bool', 'r_byte', 'r_bytes', 'r_ctype', 'r_float', 'r_float64', 'r_floats', 'r_floats64', 'r_int', 'r_int16', 'r_int64', 'r_int8', 'r_ints', 'r_ints16', 'r_ints64', 'r_ints8', 'r_string', 'r_uint', 'r_uint16', 'r_uint64', 'r_uints', 'r_uints16', 'r_uints64', 'r_vec2', 'r_vec3', 'resume_sound', 'run_time', 'set_fps', 'set_log_level', 'set_sound_volume', 'set_window_flag', 'set_window_icon', 'set_window_monitor', 'set_window_position', 'set_window_size', 'set_window_title', 'sound_deinit', 'sound_init', 'stop_multisound', 'stop_sound', 'system_name', 'take_screenshot', 'toggle_mouse', 'unload_sound', 'unload_texture', 'vec2', 'vec2_add', 'vec2_add_value', 'vec2_closest', 'vec2_distance', 'vec2_divide', 'vec2_length', 'vec2_length_sqr', 'vec2_multiply', 'vec2_multiply_value', 'vec2_subtract', 'vec2_subtract_value', 'vec3', 'vec3_add', 'vec3_add_value', 'vec3_closest', 'vec3_distance', 'vec3_divide', 'vec3_length', 'vec3_length_sqr', 'vec3_multiply', 'vec3_multiply_value', 'vec3_subtract', 'vec3_subtract_value', 'w', 'w_bool', 'w_byte', 'w_bytes', 'w_ctype', 'w_float', 'w_float64', 'w_floats', 'w_floats64', 'w_int', 'w_int16', 'w_int64', 'w_int8', 'w_ints', 'w_ints16', 'w_ints64', 'w_ints8', 'w_string', 'w_uint', 'w_uint16', 'w_uint64', 'w_uints', 'w_uints16', 'w_uints64', 'w_vec2', 'w_vec3', 'world_to_screen', 'world_to_screen_noexc']


class _Process(TypedDict):
    name: str
    pid: int
    debug: bool
    handle: int

class _Module(TypedDict):
    name: str
    base: int
    end: int
    size: int

class _Page(TypedDict):
    start: int
    end: int
    size: int

class _Rectangle(TypedDict):
    x: float
    y: float
    width: float
    height: float

class _Texture(TypedDict):
    id: int
    width: int
    height: int
    mipmap: int
    format: int

class _Vector2(TypedDict):
    x: float
    y: float

class _Vector3(TypedDict):
    x: float
    y: float
    z: float

class _Pixel(TypedDict):
    x: int
    y: int
    color: _Color

class _Color(TypedDict):
    r: int
    g: int
    b: int
    a: int