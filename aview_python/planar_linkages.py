import Adams

class PlanarLinkage:
    def __init__(self,model_name,points,links,joints):
        self.points_data = points
        self.links_data = links
        self.joints_data = joints
        self.model = Adams.Models.create(name=model_name)
        self.model_name = model_name
        self.material = self.model.Materials.create(name='steel', 
                                                    youngs_modulus = 2.07E+07, 
                                                    poissons_ratio = 0.29, 
                                                    density = 7.801E-06)
        self.gravity =  self.model.Forces.createGravity(name="gravity", 
                                                        xyz_component_gravity = [0,-9810,0]) 
        self.LINK_WIDTH = 5
        self.LINK_DEPTH = 2

    def create_parametrized_linkage(self):
        self.create_points()
        self.create_links()
        self.create_joints()

    def create_points(self):
        points = {}
        for point_name,point_coords in self.points_data.items():
            _point = self.model.ground_part.DesignPoints.create(name=point_name, location=point_coords)
            points.update({point_name:_point})
        self.points = points
        
    def create_links(self):
        self.parts = {}
        for link_name, base_points in self.links_data.items():
            part_k = self.model.Parts.createRigidBody(name=link_name, material_type=self.material)
            if len(base_points) > 2:
                all_markers = []
                for point in base_points:
                    mk_loc = Adams.expression(f"(LOC_RELATIVE_TO({{0.0, 0.0, 0.0}}, .{self.model_name}.ground.{point}))")
                    mk  = part_k.Markers.create(name= f"Marker_{link_name}{point}", 
                                                location=mk_loc,
                                                name_visibility="off"
                                                )
                    all_markers.append( mk )
                                        
                link_k = part_k.Geometries.createPlate(name = link_name, 
                                    markers = all_markers, 
                                    width = self.LINK_WIDTH, 
                                    radius = self.LINK_WIDTH/2)
            else:
                mi_loc = Adams.expression(f"(LOC_RELATIVE_TO({{0.0, 0.0, 0.0}}, .{self.model_name}.ground.{base_points[0]}))")
                mj_loc = Adams.expression(f"(LOC_RELATIVE_TO({{0.0, 0.0, 0.0}}, .{self.model_name}.ground.{base_points[1]}))")
                mi_ori = Adams.expression(f'(ORI_ALONG_AXIS(.{self.model_name}.ground.{base_points[0]}, .{self.model_name}.ground.{base_points[1]}, "X"))')
                mj_ori = Adams.expression(f'(ORI_ALONG_AXIS(.{self.model_name}.ground.{base_points[0]}, .{self.model_name}.ground.{base_points[1]}, "X"))')
                marker_i = part_k.Markers.create(name= f"Marker_{link_name}I", location=mi_loc, orientation=mi_ori, name_visibility="off")
                marker_j = part_k.Markers.create(name= f"Marker_{link_name}J", location=mj_loc, orientation=mj_ori, name_visibility="off")
                link_k = part_k.Geometries.createLink(name = link_name, 
                                                    i_marker = marker_i, 
                                                    j_marker = marker_j, 
                                                    width = self.LINK_WIDTH, 
                                                    depth= self.LINK_DEPTH)
            self.parts.update({link_name: part_k})
        
            
    def create_joints(self):
        self.joints = {}
        for joint_name, joint_data in self.joints_data.items():
            link_A, link_B, point = joint_data
            mi_loc = Adams.expression(f"(LOC_RELATIVE_TO({{0.0, 0.0, 0.0}}, .{self.model_name}.ground.{point}))")
            mj_loc = Adams.expression(f"(LOC_RELATIVE_TO({{0.0, 0.0, 0.0}}, .{self.model_name}.ground.{point}))")
            marker_i = self.model.Parts[link_A].Markers.create(name= f"Marker_for_{joint_name}_{link_A}", location=mi_loc, name_visibility="off", visibility="off")
            marker_j = self.model.Parts[link_B].Markers.create(name= f"Marker_for_{joint_name}_{link_B}", location=mj_loc, name_visibility="off", visibility="off")
            joint_k = self.model.Constraints.createRevolute(name = joint_name, 
                                                            i_marker = marker_i,
                                                            j_marker = marker_j)
            self.joints.update({joint_name: joint_k})
    
