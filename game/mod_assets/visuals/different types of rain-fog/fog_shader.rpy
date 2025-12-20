init python:

    #Credit to deusnovus for the original shader (https://www.shadertoy.com/view/7ldGWf)
    renpy.register_shader("shaders.fog",
        variables="""
            uniform float u_time;
            uniform vec2 u_model_size;

            varying vec2 v_tex_coord;
            attribute vec2 a_tex_coord;

            uniform vec3 u_fog_color;
            uniform vec3 u_bg_color;
            uniform float u_zoom;
            uniform float u_intensity;
            uniform float u_alpha;
        """,
        fragment_functions="""
            vec2 random(vec2 st){
                st = vec2(dot(st, vec2(127.1, 311.78)),
                        dot(st, vec2(269.5,183.3)));
                return -1. + 2. * fract(sin(st) * 7.);
            }

            float noise(vec2 st){
                vec2 i = floor(st);
                vec2 f = fract(st);

                //Smoothstep without clamping
                vec2 u = f * f * (3. - 2. * f);

                return mix( mix( dot( random(i + vec2(0.0,0.0) ), f - vec2(0.0,0.0)),
                    dot( random(i + vec2(1.0,0.0) ), f - vec2(1.0,0.0) ), u.x),
                    mix( dot( random(i + vec2(0.0,1.0) ), f - vec2(0.0,1.0) ),
                    dot( random(i + vec2(1.0,1.0) ), f - vec2(1.0,1.0) ), u.x), u.y);
            }

            float fractal_brownian_motion(vec2 coord) {
                float value = 0.0;
                float scale = 0.2;
                for (int i = 0; i < 4; i++) {
                    value += noise(coord) * scale;
                    coord *= 2.0;
                    scale *= 0.5;
                }
                return value + 0.2;
            }
        """,
        vertex_200="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_200="""
            vec2 uv = (v_tex_coord * u_model_size) / u_model_size;
            uv *= u_model_size / u_model_size.y;

            vec2 pos = vec2(uv * u_zoom);
            vec2 motion = vec2(fractal_brownian_motion(pos + vec2(u_time * -0.5, u_time * -0.3)));
            float final = fractal_brownian_motion(pos + motion) * u_intensity;

            vec3 final_color = mix(u_bg_color, u_fog_color, final);

            gl_FragColor = vec4(final_color, u_alpha);
        """
    )

    class Fog(renpy.Displayable):
        """
        This class allows you to define a new fog shader you can use to...well, make a
        fog effect :kekw: Example is below:
            `image fog = Fog(parameters)`

        Before anything, you need to know that this shader might not exactly display the fog
        the way you want it to be, as it also can darken/lighten the images behind it. While
        real fog actually impacts how we can see things, some parameters combinations might not
        render well. Because of that, I advise you to just spend time trying things until the fog
        effect looks alright for your needs.

        Parameters are the following:
        - `fog_color`: The color of the fog itself. It uses three decimal values from 0.0 to 1.0
        representing the red, green and blue channels respectively. Defaults to `(0.42, 0.40, 0.47)` (gray).
            
        - `bg_color`: The color of all the pixels that aren't part of the fog at each frame. While
        this shouldn't be changed, it *might* create cool looking things (maybe, hasn't been tested).
        Try at your own risk :kek: Defaults to `black`.

        - `zoom`: How much the fog displayable is zoomed. Minimum value should always be 1.0, where
        the fog is extremely zoomed in, so you won't see much details. On the other hand, a higher value,
        by already adding 1 for example, adds more details to the shader as it's zoomed out even more.
        Defaults to `3.0` for a decent balance.

        - `intensity`: How intense the fog visibility is. The higher the value is, the more bright the
        fog will appear (and the more it will tend to a white hue). Defaults to `4.0`. There aren't really
        any boundaries for this variable, just don't exaggerate it either LOL (maximum of 8-10 should do it).

        - `opacity`: Defines how the fog should render, mostly when used with other displayables.
        Since you'll most of the time want the shader to display above other images, you need to specify
        how this effect should look on top of them. 
        An opacity which value is 0.0 (the minimum) will actually affect the look of the displayables
        behind it (when I tested it, it was making them WAY brighter), hence why I don't recommend using
        a value any lower than 0.3 at best. The maximum, 1.0, simply makes everything opaque, so you'll 
        only be able to see the fog and it's defined `bg_color` (everything behind it won't be visible).

        The last two parameters, width and height, should never be changed unless you're using a different
        Ren'Py project resolution (other than 1280x720). The reason for that is since the shader is drawn
        in a rectangle type of shape, if, for example, you wanted to only show the top half of a bg having
        the fog, you would see the horizontal line representing the outline of the shader image, and it looks
        UGLY. Can always be changed to show it in a specific frame though, like an animated background or anything
        like that for example.

        If you have any troubles or questions regarding the effect, contact me on Discord: iitzwolfyy_ and I'll
        try my best to solve your problem.  
        """
        def __init__(self, 
                        fog_color=(0.42, 0.40, 0.47),
                        bg_color=(0.0, 0.0, 0.0),
                        zoom=3.0,       #Minimum to 1.0
                        intensity=4.0,  #No boundaries, just don't exaggerate it
                        opacity=0.5,    # 0.3 <= value <= 1.0
                        width=1280,     
                        height=720):
            super(Fog, self).__init__()
            self.fog_color = fog_color
            self.bg_color = bg_color
            self.zoom = float(zoom)
            self.intensity = float(intensity)
            self.opacity = float(opacity)
            self.width = width
            self.height = height
            self.child = Solid("#000", xysize=(self.width, self.height))
            self.start_time = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            
            elapsed = st - self.start_time
            r1 = renpy.render(self.child, self.width, self.height, st, at)
            rv = renpy.Render(self.width, self.height)
            rv.blit(r1, (0, 0))
            rv.mesh = True
            rv.add_shader("shaders.fog")
            rv.add_uniform("u_time", elapsed)
            rv.add_uniform("u_fog_color", self.fog_color)
            rv.add_uniform("u_bg_color", self.bg_color)
            rv.add_uniform("u_zoom", self.zoom)
            rv.add_uniform("u_alpha", self.opacity)
            rv.add_uniform("u_intensity", self.intensity)
            renpy.redraw(self, 0)
            return rv

#This uses default parameters. To change specific ones, specify their name and their value:
#   `image fog = Fog(opacity=0.7)` This only changes `opacity` to 0.7.
image fog = Fog()